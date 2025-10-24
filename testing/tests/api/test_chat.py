import pytest
import requests
import logging
import os
from faker import Faker

logger = logging.getLogger(__name__)
fake = Faker()

@pytest.fixture(scope='session', autouse=True)
def common_variables():
    urls = getattr(pytest, 'urls', None)
    token = getattr(pytest, 'admin_bearer', None)
    yield urls, token

# Register Users without login
@pytest.mark.api
@pytest.mark.users
def test_post_chat(common_variables):
    urls, token, = common_variables
    register_url = urls['api_chat']

    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    payload = {
      "title": "learn to how to do testing",
      "current_level": "basic",
      "resources": "books, youtube, google",
      "target_date": "2026-10-24",
      "days_per_week": 5,
      "hours_per_day": 3,
      "status": "active",
      "ia_suggestion": ""
    }

    response = requests.post(
        url=register_url,
        headers=header,
        json=payload
    )

    logger.info(f'Payload {payload}')
    logger.info(f'Status code {response.status_code}')
    logger.info(f'Response {response.json()}')

    assert response.status_code == 200
    content = response.json()['reply']
    assert not content.isspace() and len(content) > 0