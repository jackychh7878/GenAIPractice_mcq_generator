import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# os.getcwd() to get current path
log_path=os.path.join(os.getcwd(), "logs")

# Create the folder based on the given path
os.makedirs(log_path, exist_ok=True)

LOG_FILEPATH=os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
