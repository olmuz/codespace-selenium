import yaml


class BasePage(object):
    def __init__(self, browser):
        self.settings = yaml.load(open('settings.yaml'))

        self.browser = browser
        self.url = None
        self.locators = {}

    def open(self):
        self.browser.get(self.url)

    def find_element(self, name):
        # searches for element on page
        return self.browser.find_element_by_xpath(self.locators[name])

    def find_elements(self, name):
        # searches for ALL elements on page
        return self.browser.find_elements_by_xpath(self.locators[name])
