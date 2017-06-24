from .base_element import BaseElement


class Link(BaseElement):
    def __init__(self, browser, text):
        locator = '//a[text() = "{}"]'.format(text)
        super(Link, self).__init__(browser, locator)



