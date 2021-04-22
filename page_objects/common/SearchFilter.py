from selenium.common.exceptions import NoSuchElementException

from locators import Common, Admin
from page_objects.BasePage import BasePage
from time import sleep


class SearchFilter(BasePage):

    def click_submit_button(self):
        self._click(Common.search_filter.submit_button)
        sleep(1)
        return self

    def input_product_name(self, product_name):
        self._input(Common.search_filter.product_name_field, product_name)
        return self

    def input_product_sku(self, product_sku):
        self._input(Common.search_filter.product_sku_field, product_sku)
        sleep(1)
        return self

    def check_name_found_product(self):
        assert 'test' in self._get_element_text(Admin.name_found_product), \
            'The name of the product you are looking for is not displayed'

    def go_to_next_previous_page(self, name_attribute):
        self._wait_for_visible(Common.pagination.next_page_button)
        sleep(1)
        self._click(Common.pagination.next_page_button)
        sleep(2)
        assert '2' in self._get_attribute_value(name_attribute, Common.pagination.current_page_number), \
            'Current page does not contain 2'
        self._click(Common.pagination.previous_page_button)
        sleep(2)
        assert '1' in self._get_attribute_value(name_attribute, Common.pagination.current_page_number), \
            'Current page does not contain 1'
        return self
