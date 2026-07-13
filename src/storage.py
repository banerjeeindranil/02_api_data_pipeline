import json
import pandas as pd
from config import RAW_USERS_PATH
from config import PROCESSED_USERS_PATH

def save_raw_users(users):
    file_path = RAW_USERS_PATH
    with open(file_path, "w") as file:
        json.dump(users, file)


def save_processed_users(users_df):
    file_path = PROCESSED_USERS_PATH
    users_df.to_parquet(file_path)