from base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, browser):
        super(LoginPage, self).__init__(browser)
        self.url = 'http://facebook.com'
        self.locators = {
            'email': 'input#email',
            'password': 'input#pass',
            'login_btn': 'input[type=submit]',
            'forgot_lnk': 'a[data-testid=forgot_account_link]'
        }

    def login(self, email, pwd):
        email_input = self.find_element('email')
        pwd_input = self.find_element('password')
        email_input.clear()
        email_input.send_keys(email)
        pwd_input.send_keys(pwd)

        self.find_element('login_btn').click()

    def forgot_account(self):
        self.find_element('forgot_lnk').click()

