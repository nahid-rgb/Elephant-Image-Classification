"""
This file defines the directory paths and file locations
required for each component of the Elephant Image Classification project.
It determines where the pipeline artifacts will be stored during each training run.
"""

from datetime import datetime
import os
from elephant_classification.constants import training_pipeline


class TrainingPipelineConfig:
    """
    Create the main configuration for the training pipeline.
    This class creates a unique artifact folder using the current timestamp.

    Example:
        artifacts/
            11_17_2026_15_30_45/
    """

    def __init__(self, timestamp=None):

        # If no timestamp is provided, use the current date & time
        if timestamp is None:
            timestamp = datetime.now()

        self.timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACTS_DIR
        self.artifact_dir = os.path.join(self.artifact_name, self.timestamp)
        self.model_dir = os.path.join(training_pipeline.FINAL_MODEL_DIR_NAME)
        self.final_model_path = os.path.join(self.model_dir,training_pipeline.MODEL_FILE_NAME)


class DataIngestionConfig:
    """
    Create all configuration paths and settings required for data ingestion.

    This class defines:
    - Where the complete dataset will be copied from the KaggleHub cache.
    - The Kaggle dataset identifier.

    Example:
        artifacts/
            11_17_2026_15_30_45/
                data_ingestion/
                    dataset/
                        train/
                            African/
                            Asian/
                        test/
                            African/
                            Asian/
    """

    def __init__(self, training_pipeline_config: TrainingPipelineConfig,kaggle_dataset_name: str):

        # Root folder for data ingestion
        # artifacts/11_17_2026_15_30_45/data_ingestion
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )

        # Path where the complete dataset from KaggleHub will be copied
        # artifacts/11_17_2026_15_30_45/data_ingestion/dataset
        self.dataset_dir: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATASET_DIR_NAME
        )

        # Kaggle dataset identifier used by KaggleHub
        self.kaggle_dataset_name: str = kaggle_dataset_name


class DataValidationConfig:
    """
    Create all configuration paths and settings required for data validation.

    This class defines:
    - Where the data validation results will be saved.
    - Where the validation status file will be generated.

    Example:
        artifacts/
            11_17_2026_15_30_45/
                data_validation/
                    validation_status.txt
    """

    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        # Root folder for data validation
        # artifacts/11_17_2026_15_30_45/data_validation
        self.data_validation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_VALIDATION_DIR_NAME
        )

        # Path where the dataset validation status will be saved
        # artifacts/11_17_2026_15_30_45/data_validation/validation_status.txt
        self.validation_status_file_path: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.VALIDATION_STATUS_FILE_NAME
        )


class DataTransformationConfig:
    """
    Create all configuration paths and settings required for data transformation.

    This class defines:
    - Where the data transformation artifacts will be stored.

    Example:
        artifacts/
            11_17_2026_15_30_45/
                data_transformation/
    """

    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        # Root folder for data transformation
        # artifacts/11_17_2026_15_30_45/data_transformation
        self.data_transformation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_TRANSFORMATION_DIR_NAME
        )


class PrepareBaseModelConfig:
    """
    Create all configuration paths and settings required for preparing the base model.

    This class defines:
    - Where the pretrained base model will be saved.

    Example:
        artifacts/
            11_17_2026_15_30_45/
                prepare_base_model/
                    base_model.keras
    """

    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        # Root folder for preparing the base model
        # artifacts/11_17_2026_15_30_45/prepare_base_model
        self.prepare_base_model_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.PREPARE_BASE_MODEL_DIR_NAME
        )

        # Path where the pretrained base model will be saved
        # artifacts/11_17_2026_15_30_45/prepare_base_model/base_model.keras
        self.base_model_path: str = os.path.join(
            self.prepare_base_model_dir,
            training_pipeline.BASE_MODEL_FILE_NAME
        )


class ModelTrainerConfig:
    """
    Create all configuration paths and settings required for model training.

    This class defines:
    - Where the trained model will be saved.

    Example:
        artifacts/
            11_17_2026_15_30_45/
                model_trainer/
                    trained_model/
                        model.keras
    """

    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        # Root folder for model training
        # artifacts/11_17_2026_15_30_45/model_trainer
        self.model_trainer_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.MODEL_TRAINER_DIR_NAME
        )

        # Path where the trained model will be saved
        # artifacts/11_17_2026_15_30_45/model_trainer/trained_model/model.keras
        self.trained_model_file_path: str = os.path.join(
            self.model_trainer_dir,
            training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR,
            training_pipeline.MODEL_FILE_NAME
        )


class ModelEvaluationConfig:
    """
    Create all configuration paths and settings required for model evaluation.

    This class defines:
    - Where the model evaluation report will be saved.

    Example:
        artifacts/
            11_17_2026_15_30_45/
                model_evaluation/
                    scores.json
    """

    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        # Root folder for model evaluation
        # artifacts/11_17_2026_15_30_45/model_evaluation
        self.model_evaluation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.MODEL_EVALUATION_DIR_NAME
        )

        # Path where the model evaluation report will be saved
        # artifacts/11_17_2026_15_30_45/model_evaluation/scores.json
        self.scores_file_path: str = os.path.join(
            self.model_evaluation_dir,
            training_pipeline.MODEL_EVALUATION_REPORT_FILE_NAME
        )
