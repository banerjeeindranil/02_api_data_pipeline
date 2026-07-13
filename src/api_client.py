import requests
from config import API_URL

def fetch_users():
    url = API_URL
    
    response = requests.get(url)
    
    if response.ok:
        return response.json()
    
    else:
        raise Exception(f"Failed to fetch users from the API {response.status_code}")