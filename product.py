from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Product():
    def __init__(self, browser, name):
        self.locator = ('//div[@class="product-info"]'
                   '[h2[@class="product-name"]'
                   '/a[text()="{0}"]]').format(name)
        self.browser = browser
        self.name = name

    @property
    def is_visible(self):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.locator)
                )
            )
        except TimeoutException:
            return False
        else:
            return True








