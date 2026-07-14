import requests
from config import API_URL
from src.logger import logger

def fetch_users():
    url = API_URL
    logger.info("Fetching users from API. . .")
    response = requests.get(url)
    
    if response.ok:
        users = response.json()
        logger.info(f"Retrieved {len(users)} users.")
        return users
    
    else:
        raise Exception(f"Failed to fetch users from the API {response.status_code}")
    
    