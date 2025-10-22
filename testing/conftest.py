from playwright.sync_api import Playwright
import pytest
import logging
import os

from utils.common_functions import get_token, load_urls

# Set log configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("test_logs.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

@pytest.fixture(scope='session', autouse=True)
def setup_session(playwright: Playwright):
    x = get_token()
    pytest.bearer = x if x else None
    pytest.urls = load_urls()