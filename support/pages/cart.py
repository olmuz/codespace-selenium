from .base_page import BasePage
import support.ui as ui

class Cart(BasePage):
    def __init__(self, browser):
        super(Cart, self).__init__(browser)
        self.url = 'http://magento-demo.lexiconn.com/checkout/cart/'
        self.locators = {
            'grand_total': '//table[@id="shopping-cart-totals-table"]'
                           '//strong[text()= "Grand Total"]'
                           '/following::span[@class="price"]',
        }

    @property
    def grand_total(self):
        return float(self.find_element('grand_total').text[1:])

    @property
    def products(self):
        return [ProductInCart(self.browser, index=i+1)
                for i in range(ProductInCart(self.browser).count)]

        # example without list comprehensions:
        # products = []
        # for i in range(ProductInCart(self.browser).count):
        #     products.append(ProductInCart(self.browser, index=i+1))
        # return products

        # list_ = []
        # for product in products:
        #     list.append(product.price)
        #
        # [product.price for product in products]



class ProductInCart(ui.BaseElement):
    def __init__(self, browser, index=None):
        locator = '//table[@id="shopping-cart-table"]' \
                  '/tbody/tr'
        if index:
            locator += "[{}]".format(index)
        super(ProductInCart, self).__init__(browser, locator)

    @property
    def price(self):
        return float(self.element.find_element_by_xpath(
            './/td[@class="product-cart-price"]'
            '//span[@class="price"]'
        ).text[1:])

    @property
    def subtotal(self):
        return float(self.element.find_element_by_xpath(
           './/td[@class="product-cart-total"]'
            '//span[@class="price"]'
        ).text[1:])

    def edit_qty(self, qty):
        input_el = self.element.find_element_by_xpath(
            './/td[@class="product-cart-actions"]/input'
        )
        input_el.clear()
        input_el.send_keys(qty)
        self.element.find_element_by_xpath(
            './/td[@class="product-cart-actions"]/button'
        ).click()

    def remove_item(self):
        self.element.find_element_by_xpath(
            './/td[contains(@class, "product-cart-remove")]/a'
        ).click()
