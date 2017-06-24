import unittest

from selenium import webdriver

from link import Link
from support.pages.login_page import LoginPage


class TestFooter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_footer_links(self):
        links = (
            # COMPANY
            'About Us',
            'Contact Us',
            'Customer Service',
            'Privacy Policy',
            # QUICK LINKS
        )

        LoginPage(self.browser).open()
        for link in links:
            Link(self.browser, link).click()
            self.assertEqual(self.browser.title, link)

