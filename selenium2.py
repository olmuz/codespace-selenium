import unittest

import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(0)
        cls.settings = yaml.load(open('settings.yaml'))

    def setUp(self):
        LoginPage(self.browser).open()

    def test_login_with_incorrect_password(self):
        LoginPage(self.browser).login('s1iderorama@gmail.com', 'codesace')
        self.assertIn('Customer Login', self.browser.title)

    def test_forgot_password(self):
        LoginPage(self.browser).forgot_account()
        self.assertIn('Forgot Your Password', self.browser.title)

    def test_hover(self):
        loc = '//a[contains(., "Accessories")]'
        element = self.browser.find_element_by_xpath(loc)
        mouse_over = ActionChains(self.browser).move_to_element(element)
        mouse_over.perform()

    def test_search(self):
        self.browser.find_element_by_css_selector('input#search').send_keys('shoes')

        options = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, '//div[@id="search_autocomplete"]/ul/li[@title]')))
        options[0].click()
        assert self.browser.find_elements_by_css_selector('a[title="Black Nolita Cami"]')

    @classmethod
    def tearDownClass(cls):
        # cls.browser.quit()
        pass
