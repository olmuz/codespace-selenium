from base_element import BaseElement


class Input(BaseElement):
    def __init__(self, browser, name, method='label'):
        locator = {
            'name' : '//input[@name = "{}"]',
            'label': '//label[. = "{}"]/following-sibling::div/input',
            'id'   : '//input[@id = "{}"]'
        }[method].format(name)
        super(Input, self).__init__(browser, locator)

    def fill(self, text):
        # fills input with text
        self.element.clear()
        self.element.send_keys(text)

# USAGE:
# Input(self.browser, 'First Name').fill('Robot')
# Input(self.browser, 'firstname', method='name').fill('Robot')