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
def api_session():
    admin_token = get_token('admin')
    tester_token = get_token('testing')
    urls = load_urls()

    if not admin_token or not tester_token:
        raise RuntimeError("Failed to fetch tokens for admin or tester roles.")

    if not urls:
        raise RuntimeError("Failed to load URLs.")

    pytest.admin_bearer = admin_token
    pytest.tester_bearer = tester_token
    pytest.urls = urls

@pytest.fixture(scope='session', autouse=True)
def setup_session(playwright: Playwright):

    width = int(os.environ.get('WINDOW_WIDTH', 1920))
    height = int(os.environ.get('WINDOW_HEIGHT', 1080))

    # Init Bearer
    browser = playwright.chromium.launch(
        headless=False,
        args=[f'--window-size={width},{height}']
    )

    context = browser.new_context(viewport=None)

    yield context

    # Close browser
    context.close()
    browser.close()