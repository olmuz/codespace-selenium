import unittest

from selenium import webdriver

from header import Header
from link import Link
from support.pages.login_page import LoginPage


class TestFooter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_footer_links(self):
        links = (
            # MEN
            'New Arrivals',
            'Shirts',
            'Blazers'
            # WOMEN
        )

        LoginPage(self.browser).open()
        for link in links:
            Link(self.browser, 'Men').hover()
            Link(self.browser, link).click()
            self.assertTrue(Header(self.browser, link).is_visible)
            self.assertIn(link, self.browser.title)


_