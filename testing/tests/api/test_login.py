import pytest
import requests
import logging

logger = logging.getLogger(__name__)


@pytest.mark.api
@pytest.mark.login
def test_valid_login():
    """
    Valid loggin test
    :return:
    """
    token = pytest.bearer
    assert token is not None

@pytest.mark.api
@pytest.mark.login
def test_invalid_login():
    urls = pytest.urls
    login_url = urls['api_login']

    username = 'Wrong user'
    password = 'Wrong password'

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

    assert response.status_code == 400
    assert response.json()['detail'] == "Invalid username or password"