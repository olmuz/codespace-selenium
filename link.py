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

    def hover(self):
        # ActionChains is used for Drag&Drop and mouse hovering
        ac = ActionChains(self.browser)
        ac.move_to_element(self.element)
        ac.perform()

    def hover_and_click(self):
        ac = ActionChains(self.browser)
        ac.move_to_element(self.element)
        ac.click()
        ac.perform()