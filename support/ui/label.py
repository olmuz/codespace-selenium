from .base_element import BaseElement


class Label(BaseElement):
    def __init__(self, browser, label):
        locator = '//label[contains(text(), "{0}")]'.format(label)
        super(Label, self).__init__(browser, locator)