from pathlib import Path
from datetime import datetime
import os

CONFIG_FILE_PATH = Path("configs/config.yaml")
ROOT_DIR = os.getcwd()


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

#Data ingestion related variables
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"

#Data Validation related variables
DATA_VALIDATION_CONFIG_KEY = 'data_validation_config'
DATA_VALIDATION_ARTIFACT_DIR = "data_validation"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY = "schema_file_name"
DATA_VALIDATION_SCHEMA_DIR_KEY = 'schema_dir'
DATA_VALIDATION_REPORT_FILE_NAME_KEY = 'report_file_name'
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY = 'report_page_file_name'
SCHEMA_COLUMNS_KEY = 'columns'
SCHEMA_NUMERICAL_COLUMNS_KEY = 'numerical_columns'
SCHEMA_CATEGORICAL_COLUMNS_KEY = 'categorical_columns'
SCHEMA_TARGET_COLUMN_KEY = 'target_column'
SCHEMA_DOMAIN_VALUE_KEY = 'domain_value'

#Data Transformation related variables
DATA_TRANSFORMATION_CONFIG_KEY = 'data_transformation_config'
DATA_TRANSFORMATION_ARTIFACT_DIR = 'data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DIR_KEY = 'transformed_dir'
DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR_KEY = "transformed_train_dir"
DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR_KEY = "transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY = "preprocessing_dir"
DATA_TRANSFORMATION_PREPROCESSED_OBJECT_FILE_NAME_KEY = "preprocessed_object_file_name"
DATASET_SCHEMA_COLUMNS_KEY = "columns"

#Model trainer related variables
MODEL_TRAINER_CONFIG_KEY = 'model_trainer_config'
MODEL_TRAINER_ARTIFACT_DIR = 'model_trainer'
MODEL_TRAINER_TRAINED_MODEL_DIR_KEY  = 'trained_model_dir'
MODEL_TRAINER_MODEL_FILE_NAME_KEY = 'model_file_name'
MODEL_TRAINER_BASE_ACCURACY_KEY = 'base_accuracy'
MODEL_TRAINER_MODEL_CONFIG_DIR_NAME_KEY = 'model_config_dir'
MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY = 'model_config_file_name'

#Model evaluation related variables
MODEL_EVALUATION_CONFIG_KEY = 'model_evaluation_config'
MODEL_EVALUATION_ARTIFACT_DIR = 'model_evaluation'
MODEL_EVALUATION_FILE_NAME_KEY = 'model_evaluation_file_name'

#Model pusher related variables
MODEL_PUSHER_CONFIG_KEY = 'model_pusher_config'
MODEL_PUSHER_ARTIFACT_DIR = 'model_pusher'
MODEL_PUSHER_EXPORT_DIR_KEY = 'model_export_dir'


BEST_MODEL_KEY = "best_model"
HISTORY_KEY = "history"
MODEL_PATH_KEY = "model_path"

EXPERIMENT_DIR_NAME="experiment"
EXPERIMENT_FILE_NAME="experiment.csv"