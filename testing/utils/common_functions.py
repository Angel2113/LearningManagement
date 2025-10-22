from dotenv import load_dotenv
from pathlib import Path
import os
import json
from requests_ntlm import HttpNtlmAuth
import requests
import logging
from urllib3 import request

# Load env variables
URLS_FILE = Path(__file__).parent / 'urls.json'
load_dotenv()
logger = logging.getLogger(__name__)


def load_urls() -> dict:
    """
        Load the URLs
    """
    with open(URLS_FILE, 'r') as file:
        data = json.load(file)
    return data


def get_token() -> str:
    """
        Get jwt token
    """
    urls = load_urls()
    login_url = urls['api_login']
    username = os.getenv('admin_user')
    password = os.getenv('admin_password')
    logger.info(f'Username {username}')
    logger.info(f'Password {password}')

    payload = {
      "username": username,
      "password": password
    }

    response = requests.post(
        url=login_url,
        json=payload
    )

    logger.info(f'Response {response.json()}')
    logger.info(f'Status code {response.status_code}')

    if response.status_code != 200:
        logger.info(f'Failed to login to {login_url}')
        return None

    return response.json()['access_token']




