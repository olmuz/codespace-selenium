from base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class RegistrationPage(BasePage):
    def __init__(self, browser):
        super(RegistrationPage, self).__init__(browser)
        self.url = 'http://magento-demo.lexiconn.com/customer/account/create/'
        self.locators = {
            # fields
            'first_name': '//input[@name="firstname"]',
            'last_name': '//input[@name="lastname"]',
            'email': '//input[@name="email"]',
            'password': '//input[@name="password"]',
            'confirmation': '//input[@name="confirmation"]',
            'newsletter_chbx': '//input[@name="is_subscribed"]',
            'register_btn': '//button[@title="Register" and @type="submit"]',

            # validation errors
            'password_error': '//div[@id="advice-validate-cpassword-confirmation"]'
        }



    def is_password_validation_error(self):
        try:
            self.find_element(self.error_locators['password'])
        except NoSuchElementException:
            return False
        else:
            return True




