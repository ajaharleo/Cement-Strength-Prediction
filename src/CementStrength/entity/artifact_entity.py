from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionArtifact:
    train_file_path: Path
    test_file_path: Path
    previous_train_file_path: Path
    is_ingested: bool
    message: str

@dataclass(frozen=True)
class DataValidationArtifact:
    schema_file_path: Path
    droppable_columns: list
    report_file_path: Path
    report_page_file_path: Path
    is_validated: bool
    message: str

@dataclass(frozen=True)
class DataTransformationArtifact:
    transformed_train_file_path: Path
    transformed_test_file_path: Path
    preprocessed_object_file_path: Path
    is_transformed: bool
    message: str

@dataclass(frozen=True)
class ModelTrainerArtifact:
    is_trained: bool
    message: str
    trained_model_file_path: Path
    train_rmse: int or float
    test_rmse: int or float
    train_accuracy: int or float
    test_accuracy: int or float
    model_accuracy: int or float

@dataclass(frozen=True)
class ModelEvaluationArtifact:
    is_model_accepted: bool
    evaluated_model_path: Path

@dataclass(frozen=True)
class ModelPusherArtifact:
    is_model_pusher: bool
    export_model_file_path: Path