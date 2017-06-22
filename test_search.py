import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(1)

    def test_search(self):
        page = LoginPage(self.browser)
        page.open()
        page.search('shoes')

        #explicitly wait example
        wait = WebDriverWait(self.browser, 10)
        try:
            options = wait.until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, page.locators['search_results'])))
        except TimeoutException:
            pass
        options[0].click()