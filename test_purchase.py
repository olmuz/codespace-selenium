import unittest
import os.path
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import support.ui as ui
import support.pages as pages

REUSE = False


class TestPurchase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if REUSE and os.path.exists('browser.session'):
            with open('browser.session') as f:
                file_content = f.read()
                session_id, session_url = file_content.split(' ')
                cls.browser = webdriver.Remote(command_executor=session_url, desired_capabilities={})
                cls.browser.session_id = session_id
        else:
            cls.browser = webdriver.Chrome()
            session_id = cls.browser.session_id
            session_url = cls.browser.command_executor._url
            with open('browser.session', 'w') as f:
                f.write("{} {}".format(session_id, session_url))
        cls.browser.implicitly_wait(1)

        #setup logging
        logging.basicConfig(level=logging.INFO,
                            filename="log.txt")
        cls.logger = logging.getLogger('tests')

    def test_purchase(self):
        # 1
        self.logger.info(" logging in with cred: ")
        pages.LoginPage(self.browser).open()
        pages.LoginPage(self.browser).login('s1iderorama@gmail.com', 'codespace')

        # 2
        self.logger.info(" navigating to Men->Blazers")
        ui.Link(self.browser, 'Men').hover()
        ui.Link(self.browser, 'Blazers').click()

        self.logger.info(" selecting product...")
        ui.Product(self.browser, 'Stretch Cotton Blazer').select()

        ui.Select(self.browser, 'Color').select_by_text('Blue')
        ui.Select(self.browser, 'Size').select_by_text('L')
        ui.Button(self.browser, 'Add to Cart').click()

        assert False
        ui.Button(self.browser, 'Proceed to Checkout').click()

        self.assertTrue(ui.Header(self.browser, 'Checkout').is_visible)

        checkout = pages.CheckoutPage(self.browser)
        # 1 billing information
        checkout.continue_checkout()

        # 2 shipping method
        ui.Checkbox(self.browser, 'Add gift options').wait_for_element_visible().click()
        checkout.continue_checkout()

        # 3 payment information
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//label[contains(text(), "Cash On Delivery ")]')
            )
        )
        checkout.continue_checkout()

        # 4 place order
        ui.Button(self.browser, 'Place Order').wait_for_element_visible(15).click()

        # 5 verify confirmation page
        self.assertTrue(
            ui.Header(self.browser, 'Your order has been received.').is_visible
        )

        order_id = pages.CheckoutPage(self.browser).get_order_id()
        pages.MyOrders(self.browser).open()
        self.assertIn(order_id,
                      pages.MyOrders(self.browser).get_orders())
