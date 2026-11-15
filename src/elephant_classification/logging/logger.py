import logging 
import os 
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# name of the log file e.g. "11_15_2026_19_22_55.log"


LOG_FOLDER_PATH = os.path.join(os.getcwd(), "logs")
# full path to the logs folder
# e.g. "D:/ML_DL_NLP_Bootcamp/Elephant-Image-Classification/logs"


os.makedirs(LOG_FOLDER_PATH, exist_ok=True)
# creates the logs folder on disk if it does not already exist
# e.g. "D:/ML_DL_NLP_Bootcamp/Elephant-Image-Classification/logs"

LOG_FILE_PATH = os.path.join(LOG_FOLDER_PATH, LOG_FILE_NAME)
# full path to the actual log file
# e.g. "D:/ML_DL_NLP_Bootcamp/Elephant-Image-Classification/logs/11_15_2026_19_22_55.log"

logging.basicConfig(
    filename=LOG_FILE_PATH,
    # Saves logs to the specified log file

    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # Defines the log message format:
    # timestamp, line number, logger name, severity level and message

    level=logging.INFO,
    # Records INFO and higher-level messages (WARNING, ERROR, CRITICAL)
     # minimum severity level to record:
    
    # DEBUG    = 10  → ignored (below INFO)
    # INFO     = 20  → recorded ← set to this
    # WARNING  = 30  → recorded
    # ERROR    = 40  → recorded
    # CRITICAL = 50  → recorded
)
# output: [2026-11-15 19:22:55,123] 25 root - INFO - Elephant image ingestion started