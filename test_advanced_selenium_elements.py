import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import support.ui as ui
import support.pages as pages
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class TestAlert(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(5)

    def test_simple_alert(self):
        # create alert with JavaScript injection
        pages.LoginPage(self.browser).open()
        self.browser.execute_script('alert("Simple alert");')
        # wait for alert
        WebDriverWait(self.browser, 5).until(
            EC.alert_is_present()
        )
        sleep(2)
        self.browser.switch_to.alert.accept()

    def test_confirmation_alert(self):
        pages.LoginPage(self.browser).open()
        self.browser.execute_script('confirm("Confirm alert");')
        # wait for alert
        WebDriverWait(self.browser, 5).until(
            EC.alert_is_present()
        )
        sleep(2)
        # Cancel alert
        self.browser.switch_to.alert.dismiss()
        # Accept alert
        self.browser.switch_to.alert.accept()

    def test_prompt_alert(self):
        pages.LoginPage(self.browser).open()
        self.browser.execute_script('prompt("Prompt alert");')
        # wait for alert
        WebDriverWait(self.browser, 5).until(
            EC.alert_is_present()
        )

        # Send some text
        alert = self.browser.switch_to.alert
        alert.send_keys('some text')
        sleep(2)
        self.browser.switch_to.alert.accept()

    def test_iframes(self):
        self.browser.get('http://jqueryui.com/autocomplete')

        self.browser.switch_to.frame(
            self.browser.find_element_by_css_selector('iframe.demo-frame')
        )
        birds = self.browser.find_element_by_css_selector('#tags')
        birds.send_keys('Python')
        birds.send_keys(Keys.ENTER)

    def test_tabs(self):
        pages.LoginPage(self.browser).open()

        # create new tab
        ac = ActionChains(self.browser)
        ac.send_keys(Keys.CONTROL)
        ac.send_keys('T')
        ac.perform()

        # switch to latest tab 1
        window_name = self.browser.window_handles[-1]
        self.browser.switch_to.window(window_name)
        pages.RegistrationPage(self.browser).open()
        self.browser.close()
        self.browser.switch_to.window(
            self.browser.window_handles[0]
        )
        self.browser.get('http://google.com')

    def test_drag_and_drop(self):
        url = 'https://www.w3schools.com/html/html5_draganddrop.asp'

        self.browser.get(url)
        ac = ActionChains(self.browser)
        ac.drag_and_drop(self.browser.find_element_by_id('drag1'),
                         self.browser.find_element_by_id('div2'))
        ac.perform()

    def test_cookies(self):
        page = pages.LoginPage(self.browser)
        page.open()
        page.login('s1iderorama@gmail.com', 'codespace')
        cookies = self.browser.get_cookies()

        self.browser.delete_all_cookies()

        page.open()
        print(cookies)
        for cookie in cookies:
            self.browser.add_cookie(cookie)
        page.open()
