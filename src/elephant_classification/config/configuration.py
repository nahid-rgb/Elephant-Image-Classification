"""
This file reads the configuration settings from YAML files
and creates configuration objects for different pipeline components.

configuration.py will:
1. Read the config.yaml file.
2. Extract the Kaggle dataset name.
3. Create a TrainingPipelineConfig object.
4. Pass the Kaggle dataset name and training configuration to DataIngestionConfig.
5. Return the DataIngestionConfig object so that data_ingestion.py can use it.
configuration.py → Reads settings and provides the required configurations to each component.
"""


import os
from pathlib import Path

from elephant_classification.constants import training_pipeline
from elephant_classification.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    PrepareBaseModelConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig
)

from elephant_classification.utils.common import read_yaml


class ConfigurationManager:
    def __init__(self, config_filepath=Path("config/config.yaml")):
        # Read the configuration file
        self.config = read_yaml(config_filepath)

        # Create the main artifact directory
        os.makedirs(training_pipeline.ARTIFACTS_DIR, exist_ok=True)

        # Create the main training pipeline configuration
        # Object of the TrainingPipelineConfig class
        self.training_pipeline_config = TrainingPipelineConfig()

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Get the data ingestion configuration.
        """

        # Get the data ingestion configuration from config.yaml
        data_ingestion_config = self.config.data_ingestion

        # Create the data ingestion configuration object
        config = DataIngestionConfig(
            training_pipeline_config=self.training_pipeline_config,
            kaggle_dataset_name=data_ingestion_config.kaggle_dataset_name
        )

        return config

    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Get the data validation configuration.
        """

        config = DataValidationConfig(
            training_pipeline_config=self.training_pipeline_config
        )

        return config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Get the data transformation configuration.
        """

        config = DataTransformationConfig(
            training_pipeline_config=self.training_pipeline_config
        )

        return config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        """
        Get the prepare base model configuration.
        """

        config = PrepareBaseModelConfig(
            training_pipeline_config=self.training_pipeline_config
        )

        return config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """
        Get the model trainer configuration.
        """

        config = ModelTrainerConfig(
            training_pipeline_config=self.training_pipeline_config
        )

        return config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """
        Get the model evaluation configuration.
        """

        config = ModelEvaluationConfig(
            training_pipeline_config=self.training_pipeline_config
        )

        return config
