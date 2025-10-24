import pytest
from playwright.sync_api import Playwright

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.urls = getattr(pytest, 'urls', None)
        self.url = self.urls['home_page']

    def load_fields(self):
        self.username_field = self.page.locator('#username')
        self.password_field = self.page.locator('#password')
        self.login_btn = self.page.locator('#btn_Login')
        self.register_btn = self.page.locator('#btn_Register')

    def goto(self):
        self.page.goto(self.url)
        self.load_fields()

    def enter_credentials(self, user, password):
        self.username_field.fill(user)
        self.password_field.fill(password)

    def click_login(self):
        self.login_btn.click()





