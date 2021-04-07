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
        browser.open(path='applications/603f46af4bc1046785bc364e/pages/603f46af4bc1046785bc3650')
        return self

    def check_custom_text_widget_benefits(self):
        assert 'קטלוג הטבות' in self._get_element_text(Admin.custom_text_widget.custom_text_widget_benefits), \
            'The custom text widget is not displayed'
        sleep(1)
        return self

    def create_new_benefit(self, cost, stock, description, name, image_name):
        self._click(Admin.benefits.button_go_to_request_benefits)
        self._switch_to_frame(Admin.benefits.create_benefit_form.frame)
        self._click(Admin.benefits.create_benefit_form.cost_field)
        self._input(Admin.benefits.create_benefit_form.cost_field, cost)
        self._click(Admin.benefits.create_benefit_form.stock_field)
        self._input(Admin.benefits.create_benefit_form.stock_field, stock)
        self._click(Admin.benefits.create_benefit_form.description_field)
        self._input(Admin.benefits.create_benefit_form.description_field, description)
        self._click(Admin.benefits.create_benefit_form.name_field)
        self._input(Admin.benefits.create_benefit_form.name_field, name)
        self._click(Admin.benefits.create_benefit_form.image_field)
        self._input(Admin.benefits.create_benefit_form.image_field, image_name)
        self._click(Admin.benefits.create_benefit_form.select_status_benefit)
        self._click(Admin.benefits.create_benefit_form.status_active)
        sleep(1)
        self._click(Admin.benefits.create_benefit_form.save_benefit_button)
        sleep(1)
        print(self._get_element_text(Admin.benefits.create_benefit_form.product_created_msg))
        assert 'Product Created' in self._get_element_text(Admin.benefits.create_benefit_form.product_created_msg), \
            'message "Product Created" is not displayed '
        self._switch_to_default()
        self._click(Admin.benefits.create_benefit_form.close_benefits_form)

    def delete_benefit(self):
        self._click_elements(Admin.benefits.preview_benefit_form, index=-1)
        sleep(10)

