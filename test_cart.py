import unittest
from selenium import webdriver
import support.ui as ui
import support.pages as pages
import logging
logging.basicConfig(level=logging.INFO)

class TestCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(1)

    def test_cart(self):
        page = pages.LoginPage(self.browser)
        page.open()
        page.login('s1iderorama@gmail.com', 'codespace')

        # navigate to Home & Decor->Electronics
        # page.navigate_to('Home & Decor->Electronics')
        # ui.Product(self.browser, '8Gb Memory Card').select()
        #
        # ui.Button(self.browser, 'Add to Cart').click()

        cart = pages.Cart(self.browser)
        cart.open()

        cart.products[0].edit_qty(2)

        self.assertEqual(
            cart.products[0].subtotal,
            cart.products[0].price * 2
        )

        logging.info([product.subtotal for product in cart.products])
        self.assertEqual(
            sum(
                [product.subtotal for product in cart.products]
            ),
            cart.grand_total
        )

