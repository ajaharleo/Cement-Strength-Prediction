import os, sys
from CementStrength.entity import DataIngestionArtifact, DataTransformationArtifact, DataValidationArtifact
from CementStrength.entity import DataTransformationConfig
from CementStrength import logger
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from CementStrength.constants import *
import numpy as np, pandas as pd
from CementStrength.utils import *

class OutlierRemover(BaseEstimator, TransformerMixin):
    def __init__(self, continuous_features:list) -> None:
        try:
            super().__init__()
            self.continuous_features = continuous_features
        except Exception as e:
            logger.info(e)

        
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        try:
            for column in self.continuous_features:
                q1 = X[column].quantile(0.25)
                q3 = X[column].quantile(0.75)
                iqr = q3-q1
                lf = q1 - 1.5*iqr
                uf = q3 + 1.5*iqr
                X = X[(X[column]>=lf) & (X[column]<=uf)]
                return X
        except Exception as e:
            logger.info(e)

class UnnecessaryFeatureRemover(BaseEstimator, TransformerMixin):
    def __init__(self, droppable_columns) -> None:
        try:
            super().__init__()
            self.droppable_columns = droppable_columns
        except Exception as e:
            logger.info(e)

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        try:
            for column in self.droppable_columns:
                if column in list(X.columns):
                    X.drop(column, axis=1, inplace=True)
            return X
        except Exception as e:
            logger.info(e)


class DataTransformation:
    def __init__(self, data_transformation_config:DataTransformationConfig,
                 data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_artifact:DataValidationArtifact ) -> None:
        try:
            logger.info(f"{'='*20} Data Transformation Log Started {'='*20}")
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact
        except Exception as e:
            logger.info(e)
    def get_transformer_object(self)-> ColumnTransformer:
        try:
            schema_file_path = self.data_validation_artifact.schema_file_path
            schema = read_yaml(schema_file_path)
            numerical_columns = schema[SCHEMA_NUMERICAL_COLUMNS_KEY]
            categorical_columns = schema[SCHEMA_CATEGORICAL_COLUMNS_KEY]
            droppable_columns = self.data_validation_artifact.droppable_columns
            num_pipeline = Pipeline(steps=[('outlier_remover', OutlierRemover(continuous_features=numerical_columns)),
                                           ('unnecessary_feature_remover', UnnecessaryFeatureRemover(droppable_columns=droppable_columns)),
                                           ('imputer', SimpleImputer(strategy='median')),
                                           ('scaling',StandardScaler())
                                          ])
            cat_pipeline = Pipeline(steps=[('unnecessary_feature_remover', UnnecessaryFeatureRemover(droppable_columns=droppable_columns)),
                                           ('imputer', SimpleImputer(strategy='most_frequent')),
                                           ('scaling', StandardScaler(with_mean=False))
                                          ])            
            logger.info(f"Categorical columns: {categorical_columns}")
            logger.info(f"Numerical columns: {numerical_columns}")
            preprocessing = ColumnTransformer(transformers=[('num_pipeline', num_pipeline, numerical_columns),
                                                            ('cat_pipeline', cat_pipeline, categorical_columns),
                                                            ])
            return preprocessing
        except Exception as e:
            logger.exception(e)

    def initiate_data_transformation(self)-> DataTransformationArtifact:
        try:
            logger.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_transformer_object()
            schema_file_path = self.data_validation_artifact.schema_file_path
            schema = read_yaml(schema_file_path)
            logger.info("Obtaining train and test dataset")
            train_df = load_data(Path(self.data_ingestion_artifact.train_file_path), Path(schema_file_path))
            test_df = load_data(Path(self.data_ingestion_artifact.test_file_path), Path(schema_file_path))
            target_column = schema[SCHEMA_TARGET_COLUMN_KEY][0]
            logger.info("Splitting the datasets into input and output features")
            X_train = train_df.drop(target_column, axis=1)
            y_train = train_df[[target_column]]
            X_test = test_df.drop(target_column, axis=1)
            y_test = test_df[[target_column]]
            logger.info("Transforming input features using preprocessing object file.")
            X_train_arr = preprocessing_obj.fit_transform(X_train)
            X_test_arr = preprocessing_obj.transform(X_test)
            logger.info("Concatenating transformed input features with output features")
            train_arr = np.array(np.c_[X_train_arr, np.array(y_train)])
            test_arr = np.array(np.c_[X_test_arr, np.array(y_test)])
            logger.info(f'type of train and test array:{type(train_arr)} & {type(test_arr)}') #
            logger.info("Saving transformed train and test datasets")
            transformed_test_dir = self.data_transformation_config.transformed_test_dir
            transformed_train_dir = self.data_transformation_config.transformed_train_dir
            transformed_test_file_path = Path(os.path.join(transformed_test_dir,
                                                      os.path.basename(self.data_ingestion_artifact.test_file_path).replace('.csv','.npz')))
            transformed_train_file_path = Path(os.path.join(transformed_train_dir,
                                                      os.path.basename(self.data_ingestion_artifact.train_file_path).replace('.csv','.npz')) )      
            save_numpy_array_data(file_path=transformed_train_file_path,array=train_arr)
            save_numpy_array_data(file_path=transformed_test_file_path,array=test_arr)
            preprocessed_object_file_path = Path(self.data_transformation_config.preprocessed_object_file_path)
            logger.info("Saving preprocesing object file")
            save_object(preprocessed_object_file_path, preprocessing_obj)
            data_transformation_artifact = DataTransformationArtifact(transformed_test_file_path=transformed_test_file_path,
                                                                    transformed_train_file_path=transformed_train_file_path,
                                                                    preprocessed_object_file_path=preprocessed_object_file_path,
                                                                    is_transformed=True,
                                                                    message="Data Transformation completed successfully.")
            logger.info(f"Data Transformation Artifact: {data_transformation_artifact}")
            return data_transformation_artifact
        except Exception as e:
            logger.exception(e)

    def __del__(self):
        logger.info(f"{'='*20}Data Transformation log completed.{'='*20} \n\n") 