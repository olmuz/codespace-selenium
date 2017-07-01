from .base_page import BasePage


class MyOrders(BasePage):
    def __init__(self, browser):
        super(MyOrders, self).__init__(browser)
        self.url = 'http://magento-demo.lexiconn.com/sales/order/history/'
        self.title = 'My Orders'
        self.locators = {
            'order_id': '//td[@class = "number"]'
        }

    def get_orders(self):
        return self.find_elements('order_id')
