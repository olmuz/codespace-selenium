from .base_element import BaseElement


class Button(BaseElement):
    def __init__(self, browser, text):
        locator = '//button[@title = "{0}"] | ' \
                  '//button//span[contains(., "{0}")] |' \
                  '//a[@class="button" and text()="{0}"]'.format(text)
        super(Button, self).__init__(browser, locator)

