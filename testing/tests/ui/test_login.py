import time

from playwright.sync_api import Page
from pages.LoginPage import LoginPage
from pages.AdminHomePage import AdminHomePage
import pytest
import allure
import os

@allure.title('Admin Login Happy Path')
@allure.description('Admin login with valid credentials')
@pytest.mark.ui
@pytest.mark.login
def test_valid_login(page: Page):
    # Get Credentials
    username = os.getenv('admin_user')
    password = os.getenv('admin_password')

    with allure.step('Open Login Page'):
        login_page = LoginPage(page)
        login_page.goto()

    with allure.step('Enter Credentials'):
        login_page.enter_credentials(user= username, password=password)

    with allure.step('Login attempt'):
        login_page.click_login()
        admin_hp = AdminHomePage(page)
        user_list = admin_hp.get_users_list()

        assert len(user_list) > 0

