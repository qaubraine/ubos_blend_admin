from locators import Common, Admin
from page_objects.BasePage import BasePage
from time import sleep
import allure


class SearchFilter(BasePage):

    def click_submit_button(self):
        with allure.step("Click 'Submit' button"):
            self._wait_for_clickable(Common.search_filter.submit_button)
            self._click(Common.search_filter.submit_button)
        return self

    def input_product_name(self, product_name):
        with allure.step("Input product name"):
            self._wait_for_clickable(Common.search_filter.product_name_field)
            self._input(Common.search_filter.product_name_field, product_name)
            sleep(1)
        return self

    def input_product_sku(self, product_sku):
        with allure.step("Input product SKU"):
            self._wait_for_clickable(Common.search_filter.product_sku_field)
            self._input(Common.search_filter.product_sku_field, product_sku)
            sleep(1)
        return self

    def check_name_found_product(self):
        with allure.step("Check name found product"):
            self._wait_for_visibility_of_element(Admin.name_found_product)
            assert 'test' in self._get_element_text(Admin.name_found_product), \
                'The product you found is not called a "test" or has an SKU not 123'

    def go_to_next_previous_page(self, name_attribute):
        with allure.step("Go to the second page with the goods"):
            self._wait_for_visibility_of_element(Common.pagination.next_page_button)
            self._click(Common.pagination.next_page_button)
            sleep(1)
            assert '2' in self._get_attribute_value(name_attribute, Common.pagination.current_page_number), \
                'Current page does not contain 2'
        with allure.step("Return to the first page"):
            self._click(Common.pagination.previous_page_button)
            assert '1' in self._get_attribute_value(name_attribute, Common.pagination.current_page_number), \
                'Current page does not contain 1'
        return self
