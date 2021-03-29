from selenium.common.exceptions import NoSuchElementException

from locators import Common
from page_objects.BasePage import BasePage
from time import sleep


class SearchFilter(BasePage):

    def click_order_search_button(self):
        self._click(Common.search_filter.order_search_button)
        return self

    def input_order_id(self, order_id):
        self._input(Common.search_filter.order_id_filter, order_id)
        return self

    def input_order_coupon(self, coupon):
        self._input(Common.search_filter.order_coupon, coupon)
        return self

    def display_processing_order(self):
        self._click(Common.search_filter.drop_down)
        self._click(Common.search_filter.processing)
        self._click(Common.search_filter.order_search_button)
        sleep(2)
        try:
            assert 'processing' in self._get_element_text(Common.status.status_is), \
                'The first order status is not - processing'
        except NoSuchElementException:
            pass
        return self

    def display_completed_order(self):
        self._click(Common.search_filter.drop_down)
        self._click(Common.search_filter.completed)
        self._click(Common.search_filter.order_search_button)
        sleep(2)
        try:
            assert 'completed' in self._get_element_text(Common.status.status_is), \
                'The first order status is not - completed'
        except NoSuchElementException:
            pass
        return self

    def display_pending_order(self):
        self._click(Common.search_filter.drop_down)
        self._click(Common.search_filter.pending)
        self._click(Common.search_filter.order_search_button)
        sleep(2)
        try:
            assert 'pending' in self._get_element_text(Common.status.status_is), \
                'The first order status is not - pending'
        except NoSuchElementException:
            pass
        return self

    def display_failed_order(self):
        self._click(Common.search_filter.drop_down)
        self._click(Common.search_filter.failed)
        self._click(Common.search_filter.order_search_button)
        sleep(2)
        try:
            self._get_element_text(Common.status.status_is)
            assert 'failed' in self._get_element_text(Common.status.status_is), \
                'The first order status is not - failed'
        except NoSuchElementException:
            pass
        return self

    def display_on_hold_order(self):
        self._click(Common.search_filter.drop_down)
        self._click(Common.search_filter.on_hold)
        self._click(Common.search_filter.order_search_button)
        sleep(2)
        try:
            self._get_element_text(Common.status.status_is)
            assert 'on-hold' in self._get_element_text(Common.status.status_is), \
                'The first order status is not - on-hold'
        except NoSuchElementException:
            pass
        return self

    def search_order_by_id(self, id_order):
        self._input(Common.search_filter.order_id_filter, id_order)
        self._click(Common.search_filter.order_search_button)
        sleep(2)
        try:
            self._get_element_text(Common.id_is.order_id)
            assert '11' in self._get_element_text(Common.id_is.order_id), \
                'Order Id does not contain 11'
        except NoSuchElementException:
            pass
        return self

    def go_to_next_previous_page(self, name_attribute):

        self._wait_for_visible(Common.pagination.next_page_button)
        sleep(2)
        self._click(Common.pagination.next_page_button)
        sleep(2)
        assert '2' in self._get_attribute_value(name_attribute, Common.pagination.current_page_number), \
            'Current page does not contain 2'
        self._click(Common.pagination.previous_page_button)
        sleep(1)
        assert '1' in self._get_attribute_value(name_attribute, Common.pagination.current_page_number), \
            'Current page does not contain 1'
        return self
