
"""
Defining common constant variables for the Elephant Image Classification project.
"""

# General project constants
PIPELINE_NAME: str = "ElephantImageClassification"
ARTIFACTS_DIR: str = "artifacts"

# Pipeline component directory names
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
PREPARE_BASE_MODEL_DIR_NAME: str = "prepare_base_model"
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_EVALUATION_DIR_NAME: str = "model_evaluation"

# Model file names
BASE_MODEL_FILE_NAME: str = "base_model.keras"
MODEL_FILE_NAME: str = "model.keras"
FINAL_MODEL_DIR_NAME: str = "final_model"

# Data Ingestion related constants
DATASET_DIR_NAME: str = "dataset"

# Model Trainer related constants
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"

# Data Validation related constants
VALIDATION_STATUS_FILE_NAME: str = "validation_status.txt"

# Model Evaluation related constants
MODEL_EVALUATION_REPORT_FILE_NAME: str = "scores.json"
