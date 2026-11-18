import sys
from elephant_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from elephant_classification.logging.logger import logging
from elephant_classification.exception.exception import ElephantClassificationException


# Execute the complete pipeline only when main.py is run directly
if __name__ == "__main__":
    try:
        # ---------------------- Data Ingestion ---------------------- #
        STAGE_NAME = "Data Ingestion stage"

        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion_artifact = data_ingestion.main()

        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        print(data_ingestion_artifact)

    except Exception as e:
        logging.exception(e)
        raise ElephantClassificationException(e, sys)
