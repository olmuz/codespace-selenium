from selenium.webdriver.common.by import By

from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):
    def __init__(self, browser):
        super(CheckoutPage, self).__init__(browser)
        self.locators = {
            'continue': '//li[contains(@class, "section") '
                        'and contains(@class, "active")]//button',
            'spinner' : '//span[@id="billing-please-wait"]',
            'order_id': '//p[contains(., "Your order # is:")]/a'
        }

    def continue_checkout(self):
        self.find_element('continue').click()
        self.wait_for_next_step()

    def wait_for_next_step(self, timeout=10):
        self.wait(timeout).until(
            EC.invisibility_of_element_located(
                (By.XPATH, self.locators['spinner'])
            )
        )

    def get_order_id(self):
        return self.find_element('order_id').text

