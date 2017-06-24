import unittest
from selenium import webdriver


class TestPurchase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_purchase_simple(self):
