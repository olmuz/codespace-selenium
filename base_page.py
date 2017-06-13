class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.url = None
        self.locators = {}

    def open(self):
        self.browser.get(self.url)

    def find_element(self, name):
        return self.browser.find_element_by_css_selector(self.locators[name])