from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base_element import BaseElement


class Product(BaseElement):
    def __init__(self, browser, name):
        self.locator = ('//div[@class="product-info"]'
                        '[h2[@class="product-name"]'
                        '/a[text()="{0}"]]').format(name)
        self.browser = browser
        self.name = name

    def select(self):
        loc = './h2[@class="product-name"]/a'
        self.element.find_element_by_xpath(loc).click()








