from src.storage import save_processed_users
from src.api_client import fetch_users
from src.transform import transform_users
from src.storage import save_raw_users
from src.logger import logger

logger.info("Starting API Data Pipeline")

try:
    users = fetch_users()

    users_df = transform_users(users)

    save_raw_users(users)
    save_processed_users(users_df)

    logger.info("Pipeline completed successfully")

except Exception as e:
    logger.error(f"Pipeline failed: {e}")
