from selenium.webdriver import ActionChains


class Link():
    def __init__(self, browser, name):
        self.browser = browser
        self.locator = '//a[text()="{0}"]'.format(name)

    @property
    def element(self):
        # returns WebElement instance
        return self.browser.find_element_by_xpath(self.locator)

    def click(self):
        self.element.click()


