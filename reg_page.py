from base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class RegistrationPage(BasePage):
    def __init__(self, browser):
        super(RegistrationPage, self).__init__(browser)
        self.url = 'http://magento-demo.lexiconn.com/'
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
            'password_error': '//div[@id="advice-validate-cpassword-confirmation"]',

            # account menu
            'menu': '//a[contains(@class, "skip-account")]',
            'menu_register': '//div[@id="header-account"]//a[text()="Register"]',
        }

    @property
    def is_password_validation_error(self):
        try:
            self.find_element('password_error')
        except NoSuchElementException:
            return False
        else:
            return True

    def open(self):
        self.browser.get(self.url)
        self.find_element('menu').click()
        self.find_element('menu_register').click()




