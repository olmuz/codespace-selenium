from .base_element import BaseElement


class Header(BaseElement):
    def __init__(self, browser, text):
        locator = '//h1[text() = "{}"]'.format(text)
        super(Header, self).__init__(browser, locator)
