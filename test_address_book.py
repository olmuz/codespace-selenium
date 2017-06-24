import unittest
from selenium import webdriver

from support.pages.login_page import LoginPage
from support.ui.button import Button
from support.ui.checkbox import Checkbox
from support.ui.link import Link
from support.ui.input import Input
from support.ui.select import Select
import support.ui


class TestAddressBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(5)

    def test_add_new_address(self):
        # 1 Do login
        LoginPage(self.browser).open()
        LoginPage(self.browser).login('s1iderorama@gmail.com', 'codespace')

        # 2 Navigate to My Address Book
        Link(self.browser, 'Address Book').click()
        Button(self.browser, 'Add New Address').click()

        #3 fill form
        test_data_input = {
            'First Name': 'Robot',
            'Last Name' : 'Bobot',
            'Company'   : 'Robotics Inc',
            'Telephone' : '123123123',
            'Fax'       : '123123412',
            # address
            'Street Address': 'Robo circle 1',
            'City'          : 'Kiev',
            'Zip'           : '12345'
        }

        for label, text in test_data_input.items():
            Input(self.browser, label).fill(text)

        Select(self.browser, 'Country').select_by_text('Ukraine')
        Checkbox(self.browser, 'Use as my default billing address').click()

