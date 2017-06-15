from base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        # super() calls parent methods
        super(LoginPage, self).__init__(browser)
        self.url = 'http://magento-demo.lexiconn.com/customer/account/login/'
        # locators mappings (css)
        self.locators = {
            'email': '//input[@name="login[username]"]',
            'password': '//input[@name="login[password]"]',
            'login_btn': '//button[@type="submit"]',
            'forgot_lnk': '//a[contains(text(), "Forgot Your Password?")]'
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

