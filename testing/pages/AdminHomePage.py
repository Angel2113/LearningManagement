import pytest
from playwright.sync_api import Playwright

class AdminHomePage:

    def __init__(self, page):
        self.page = page
        self.urls = getattr(pytest, 'urls', None)
        self.url = self.urls['home_page']

    def get_users_list(self):
        self.page.wait_for_selector('h3', state='visible')
        self.users_list = self.page.locator('h3').all()
        return self.users_list