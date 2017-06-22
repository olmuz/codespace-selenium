import unittest

import yaml
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from product import Product
from link import Link


class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.settings = yaml.load(open('settings.yaml'))
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(cls.settings['implicit_timeout'])

    def test_search(self):
        page = LoginPage(self.browser)
        page.open()
        page.search('shoes')

        #explicitly wait example
        timeout = self.settings['explicit_timeout']
        wait = WebDriverWait(self.browser, timeout)
        try:
            options = wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, page.locators['search_results'])))
        except TimeoutException:
            pass
        options[0].click()

        self.assertTrue(Product(self.browser, 'Black Nolita Cami').is_visible)

    def test_navigation(self):
        LoginPage(self.browser).open()
        Link(self.browser, 'Accessories').hover()
        Link(self.browser, 'Shoes').click()

        self.assertTrue(
            Product(self.browser, 'Ann Ankle Boot').is_visible)