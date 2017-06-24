import unittest

from selenium import webdriver
import support.ui as ui
import support.pages as pages


class TestPurchase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_purchase(self):
        pages.LoginPage(self.browser).open()
        pages.LoginPage(self.browser).login('s1iderorama@gmail.com', 'codespace')

        ui.Link(self.browser, 'Accessories').hover()
        ui.Link(self.browser, 'Jewelry').click()

        ui.Product(self.browser, 'Swing Time Earrings').select()
