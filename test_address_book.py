import unittest
from selenium import webdriver

from support.pages.login_page import LoginPage
from support.ui.link import Link
from support.ui.input import Input


class TestAddressBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_add_new_address(self):
        LoginPage(self.browser).open()
        LoginPage(self.browser).login('s1iderorama@gmail.com', 'codespace')
        Link(self.browser, 'Address Book').click()

        Input(self.browser, 'firstname').fill('Robot')
        Input(self.browser, 'lastname').fill('Bobot')
        #2 Navigate to My Address Book
        #3 fill form