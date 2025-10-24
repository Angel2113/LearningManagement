import pytest
import requests
import logging
import os
from faker import Faker

logger = logging.getLogger(__name__)
fake = Faker()


def read_user(user_name: str):
    urls = getattr(pytest, 'urls', None)
    token = getattr(pytest, 'admin_bearer', None)
    users_url = f'{urls['api_users']}/{user_name}'

    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        url=users_url,
        headers=header
    )

    return response

@pytest.fixture(scope='session', autouse=True)
def common_variables():
    urls = getattr(pytest, 'urls', None)
    token = getattr(pytest, 'admin_bearer', None)

    register_pass = fake.pystr(min_chars=8, max_chars=12)

    payload = {
        "username": fake.pystr(min_chars=8, max_chars=12),
        "email": fake.email(),
        "password": register_pass,
        "password_confirmation": register_pass,
        "role": "user"
    }

    yield urls, token, payload

# Register Users without login
@pytest.mark.api
@pytest.mark.users
def test_register_user(common_variables):
    """
    Register a user without login
    :return:
    """
    urls, _, payload = common_variables
    register_url = urls['api_register']

    response = requests.post(
        url=register_url,
        json=payload
    )

    logger.info(f'Payload {payload}')
    logger.info(f'Response {response.json()}')
    logger.info(f'Status code {response.status_code}')

    assert response.status_code == 200
    assert response.json()['message'] == "User created successfully"


# Create Users
@pytest.mark.api
@pytest.mark.users
def test_create_user(common_variables):
    urls, token, _ = common_variables
    users_url = urls['api_users']
    user_pass = fake.pystr(min_chars=8, max_chars=20)

    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "username": fake.pystr(min_chars=8, max_chars=20),
        "email": fake.email(),
        "password": user_pass,
        "password_confirmation": user_pass,
        "role": "user"
    }

    response = requests.post(
        url=users_url,
        headers=header,
        json=payload
    )

    logger.info(f'Payload {payload}')
    logger.info(f'Response {response.json()}')
    logger.info(f'Status code {response.status_code}')

    assert response.status_code == 200
    assert response.json()['message'] == "User created successfully"

# Read Users
@pytest.mark.api
@pytest.mark.users
def test_read_users(common_variables):
    urls, token, _ = common_variables
    user = os.getenv('admin_user')
    response = read_user(user)

    assert response.status_code == 200
    assert response.json()["role"] ==  "admin"
    assert response.json()["username"] ==  user

# Read All Users
@pytest.mark.api
@pytest.mark.users
def test_read_all_users(common_variables):
    urls, token, _ = common_variables
    users_url = urls['api_users']

    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        url=users_url,
        headers=header
    )

    logger.info(f'Token {token}')
    logger.info(f'URL {users_url}')
    logger.info(f'Response {response.json()}')
    logger.info(f'Status code {response.status_code}')

    assert response.status_code == 200
    assert len(list(response.json())) >= 1

# Update Users
@pytest.mark.api
@pytest.mark.users
def test_put_users(common_variables):
    urls, token, payload = common_variables

    user_id = read_user(payload['username']).json()['id']
    users_url = f'{urls['api_users']}/{user_id}'

    # update user
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    new_payload = {
        "email": fake.email()
    }

    response = requests.put(
        url=users_url,
        headers=header,
        json=new_payload
    )

    logger.info('Updating user')
    logger.info(f'URL {users_url}')
    logger.info(f'Payload {new_payload}')
    logger.info(f'Status code {response.status_code}')
    logger.info(f'Response {response.json()}')
    assert response.status_code == 200


# Delete Users
@pytest.mark.api
@pytest.mark.users
def test_delete_users(common_variables):
    urls, token, payload = common_variables

    user_id = read_user(payload['username']).json()['id']
    users_url = f'{urls['api_users']}/{user_id}'

    # Delete user
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.delete(
        url=users_url,
        headers=header,
    )


    logger.info('Delete user')
    logger.info(f'URL {users_url}')
    logger.info(f'Status code {response.status_code}')
    logger.info(f'Response {response.json()}')


    assert response.status_code == 200

