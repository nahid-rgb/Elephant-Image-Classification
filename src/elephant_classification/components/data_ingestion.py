
import os
import sys
import shutil
import kagglehub # Copy the complete dataset folder.

from elephant_classification.exception.exception import ElephantClassificationException
from elephant_classification.logging.logger import logging

from elephant_classification.entity.config_entity import DataIngestionConfig
from elephant_classification.entity.artifact_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        """
        Initialize the Data Ingestion class with the required configuration.
        """
        try:
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise ElephantClassificationException(e, sys)

    def download_dataset(self):
        """
        Download or access the Elephant dataset using KaggleHub.
        Return the path of the dataset folder.
        """
        try:
            kaggle_dataset_name = self.data_ingestion_config.kaggle_dataset_name

            logging.info(f"Downloading dataset from KaggleHub: {kaggle_dataset_name}")

            # KaggleHub downloads the dataset or uses its cached version
            download_path = kagglehub.dataset_download(kaggle_dataset_name)

            # Actual dataset folder inside the KaggleHub download directory
            dataset_path = os.path.join(download_path, "dataset")

            # Check whether the train and test folders exist
            if not os.path.isdir(os.path.join(dataset_path, "train")):
                raise FileNotFoundError("Training dataset folder not found")

            if not os.path.isdir(os.path.join(dataset_path, "test")):
                raise FileNotFoundError("Testing dataset folder not found")

            logging.info(f"Dataset accessed successfully: {dataset_path}")

            return dataset_path

        except Exception as e:
            raise ElephantClassificationException(e, sys)

    def copy_dataset_to_artifacts(self, dataset_path: str):
        """
        Copy the complete dataset into the project's artifact directory.
        Preserve the original train and test folder structure.
        """
        try:
            destination_path = self.data_ingestion_config.dataset_dir
            # Destination path where the complete dataset will be copied
            # Example: artifacts/11_18_2026_18_30_45/data_ingestion/dataset

            # Create the data ingestion directory if it does not exist
            # Example: artifacts/11_18_2026_18_30_45/data_ingestion
            os.makedirs(self.data_ingestion_config.data_ingestion_dir, exist_ok=True)

            logging.info(f"Copying dataset into: {destination_path}")

            # Copy the complete dataset from KaggleHub cache to the artifacts directory
            # C:/Users/rmahf/.cache/kagglehub/datasets/vivmankar/asian-vs-african-elephant-image-classification/versions/1
            # Destination: artifacts/11_18_2026_18_30_45/data_ingestion/dataset
            # Existing train, test and class folders are preserved
            shutil.copytree(dataset_path, destination_path, dirs_exist_ok=True)

            logging.info("Dataset copied successfully into artifacts")

            return destination_path

        except Exception as e:
            raise ElephantClassificationException(e, sys)

    def initiate_data_ingestion(self):
        """
        Execute the complete data ingestion pipeline:
        1. Access the dataset using KaggleHub.
        2. Copy the dataset into the artifact directory.
        3. Return the dataset directory path as a DataIngestionArtifact.
        """
        try:
            dataset_path = self.download_dataset()
            copied_dataset_path = self.copy_dataset_to_artifacts(dataset_path)
            data_ingestion_artifact = DataIngestionArtifact(dataset_dir=copied_dataset_path)
            # Store the copied dataset directory path in the DataIngestionArtifact object
          

            logging.info("Data ingestion completed successfully")

            return data_ingestion_artifact

        except Exception as e:
            raise ElephantClassificationException(e, sys)
