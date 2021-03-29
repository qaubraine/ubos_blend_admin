from locators import Admin
from .BasePage import BasePage
from time import sleep
import pickle


class AdminPage(BasePage):

    def open_admin_page(self, browser):
        """adding cookies for authorization from the cookie.pkl file"""
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            browser.add_cookie(cookie)
        """"go to the admin page. url + path"""
        browser.open(path='applications/5ffdc4ce2a95b879d86624d4/pages/6034cb2cbb5df115a30cabd8')
        sleep(5)
        return self

    def open_page_subscriptions(self):
        self._click(Admin.canvas_widgets_from_orders_page.custom_button_widget_subscriptions)
        sleep(5)
        return self

    def open_page_orders(self):
        self._click(Admin.canvas_widgets_from_subscription_page.custom_button_widget_orders)
        sleep(5)
        return self

    def check_custom_text_widget_orders(self):
        assert 'הזמנות' in self._get_element_text(Admin.custom_text_widget.custom_text_widget_orders), \
            'The custom text widget is not displayed'
        sleep(1)
        return self

    def check_custom_text_widget_subscriptions(self):
        assert 'מנויים' in self._get_element_text(Admin.custom_text_widget.custom_text_widget_subscriptions), \
            'The custom text widget is not displayed'
        sleep(1)
        return self

    def open_details_order(self, value):
        self._click(Admin.order.button_order_details)
        sleep(20)
        self._switch_to_frame(Admin.order.iframe_orders)
        sleep(6)
        self._wait_for_visible(Admin.order.year)
        assert '21' in self._get_attribute_value(value, Admin.order.year), 'Current page does not contain year - 21'
        self._click(Admin.order.button_notes)
        sleep(10)
        self._wait_for_visible(Admin.order.notes)
        assert 'Notes' in self._get_element_text(Admin.order.notes), 'Current page does not contain - Notes'

    def open_details_subscription(self, value):
        self._click(Admin.subscription.button_subscription_details)
        sleep(20)
        self._switch_to_frame(Admin.subscription.iframe_subscriptions)
        print('switched')
        sleep(6)
        self._wait_for_visible(Admin.subscription.year)
        assert '21' in self._get_attribute_value(value,
                                                 Admin.subscription.year), 'Current page does not contain year - 21'
        self._click(Admin.subscription.button_notes)
        sleep(10)
        self._wait_for_visible(Admin.subscription.notes)
        assert 'Notes' in self._get_element_text(Admin.subscription.notes), 'Current page does not contain - Notes'
