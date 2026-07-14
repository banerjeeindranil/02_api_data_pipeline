import json
import pandas as pd
from config import RAW_USERS_PATH
from config import PROCESSED_USERS_PATH
from src.logger import logger

def save_raw_users(users):
    logger.info("Saving raw users JSON. . . ")
    file_path = RAW_USERS_PATH
    with open(file_path, "w") as file:
        json.dump(users, file)
    logger.info("Raw users JSON saved successfully")


def save_processed_users(users_df):
    logger.info("Saving processed users Parquet. . .")
    file_path = PROCESSED_USERS_PATH
    logger.info("Processed users Parquet saved successfully.")