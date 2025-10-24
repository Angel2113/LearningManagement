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

def get_all_goals():
    urls = getattr(pytest, 'urls', None)
    token = getattr(pytest, 'tester_bearer', None)
    goals_url = f'{urls['api_goals']}'

    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        url=goals_url,
        headers=header
    )
    logger.info(f'Get all Goals URL {goals_url}')
    logger.info(f'Get all Goals {response.json()}')
    return response.json()

@pytest.fixture(scope='session', autouse=True)
def common_variables():
    urls = getattr(pytest, 'urls', None)
    token = getattr(pytest, 'tester_bearer', None)
    user_name = os.getenv('testing_user')
    user = read_user(user_name).json()

    yield urls, token, user

# Create Users
@pytest.mark.api
@pytest.mark.users
def test_create_goal(common_variables):
    urls, token, user_info = common_variables
    users_url = urls['api_goals']

    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    payload = {
      "title": "how to do testing",
      "current_level": "basic",
      "resources": "books, youtube, google",
      "target_date": "2025-10-24",
      "days_per_week": 5,
      "hours_per_day": 2,
      "status": "active",
      "ia_suggestion": ""
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
    assert response.json()['message'] == "Goal created successfully"

# Read Goal
@pytest.mark.api
@pytest.mark.users
def test_read_goal(common_variables):
    urls, token, _ = common_variables
    goals = get_all_goals()
    logger.info(f'All Goals {goals}')

    goal_id = goals[0]['id']
    goal_url = f'{urls['api_goals']}/{goal_id}'

    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        url=goal_url,
        headers = header
    )

    logger.info(f'Response Code {response.status_code}')
    logger.info(f'Content  {response.json()}')
    assert response.status_code == 200

# Read All Goals
@pytest.mark.api
@pytest.mark.users
def test_read_all_goals(common_variables):
    urls, token, _ = common_variables
    users_url = urls['api_users']

    goals = get_all_goals()

    assert len(goals) >= 1

# Update Goal
@pytest.mark.api
@pytest.mark.users
def test_put_goal(common_variables):
    urls, token, user = common_variables

    goal_id = get_all_goals()[0]['id']
    goal_url = f'{urls['api_goals']}/{goal_id}'

    # update goal
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    new_payload = {
      "title": "Update",
      "current_level": "inter",
      "resources": "Books, Youtube",
      "target_date": "2027-10-24",
      "days_per_week": 3,
      "hours_per_day": 3,
      "status": "active"
    }

    response = requests.put(
        url=goal_url,
        headers=header,
        json=new_payload
    )


    logger.info('Updating Goal')
    logger.info(f'URL {goal_url}')
    logger.info(f'Payload {new_payload}')
    logger.info(f'Status code {response.status_code}')
    logger.info(f'Response {response.json()}')

    assert response.status_code == 200


# Update Users
@pytest.mark.api
@pytest.mark.users
def test_delete_users(common_variables):
    urls, token, user = common_variables
    goal_id = get_all_goals()[0]['id']
    goal_url = f'{urls['api_goals']}/{goal_id}'

    # Delete Goal
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.delete(
        url=goal_url,
        headers=header,
    )

    logger.info('Delete Goal')
    logger.info(f'URL {goal_url}')
    logger.info(f'Status code {response.status_code}')
    logger.info(f'Response {response.json()}')

    assert response.status_code == 200