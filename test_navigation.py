import unittest
from selenium import webdriver
from link import Link
from header import Header
from login_page import LoginPage


class TestFooter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_footer_links(self):
        links = (
            # MEN
            'New Arrivals',
            '...',
            # WOMEN
        )

        LoginPage(self.browser).open()
        for link in links:
            hover()
            click()
            self.assertEqual(Header(self.browser).is_visible))


