from base_element import BaseElement


class Select(BaseElement):
    def __init__(self, browser, label):
        locator = '//label[contains(., "{}")]/following-sibling' \
                  '::div/select'.format(label)
        super(Select, self).__init__(browser, locator)

    @property
    def options(self):
        # returns list of options (WebElement)
        locator = self.locator + '/option'
        return self.browser.find_elements_by_xpath(locator)

    def select_by_index(self, index):
        self.options[index].click()

    def select_by_text(self, text):
        locator = self.locator + '/option[text() = "{}"]'.format(text)
        self.browser.find_element_by_xpath(locator).click()
