from base_element import BaseElement


class Button(BaseElement):
    def __init__(self, browser, title):
        locator = '//button[@title = "{}"]'.format(title)
        super(Button, self).__init__(browser, locator)

