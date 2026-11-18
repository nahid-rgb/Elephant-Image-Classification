import sys
from elephant_classification.exception.exception import ElephantClassificationException
from elephant_classification.config.configuration import ConfigurationManager
from elephant_classification.components.data_ingestion import DataIngestion
from elephant_classification.logging.logger import logging


STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        """
        Execute the Data Ingestion stage.
        """
        try:
            # Create ConfigurationManager to get the Data Ingestion configuration
            config = ConfigurationManager()

            # Get the Data Ingestion configuration from config.yaml and config_entity.py
            data_ingestion_config = config.get_data_ingestion_config()

            # Initialize the Data Ingestion component with the required configuration
            data_ingestion = DataIngestion(data_ingestion_config)

            # Execute Data Ingestion and receive the generated artifact
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            # Return the Data Ingestion artifact for the next pipeline stage
            return data_ingestion_artifact

        except Exception as e:
            logging.exception(e)
            raise e


# Execute this stage independently when this file is run directly
if __name__ == "__main__":
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion_artifact = data_ingestion.main()

        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")

        print(data_ingestion_artifact)

    except Exception as e:
        logging.exception(e)
        raise ElephantClassificationException(e, sys)
