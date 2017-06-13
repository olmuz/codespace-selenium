import unittest
from selenium import webdriver
from login_page import LoginPage


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(2)
        LoginPage(cls.browser).open()

    def test_login_with_incorrect_password(self):
        LoginPage(self.browser).login('denis.zvezdov', 'pwd')
        self.assertIn('Log into Facebook', self.browser.title)

    def test_forgot_password(self):
        LoginPage(self.browser).forgot_account()
        self.assertIn('Forgot Password', self.browser.title)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
