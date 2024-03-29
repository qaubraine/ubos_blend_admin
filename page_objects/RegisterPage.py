import allure

from locators import Register
from .BasePage import BasePage
from time import sleep


class RegisterPage(BasePage):

    def open_login_page(self):
        with allure.step("Select the type of account - User"):
            self._wait_for_visibility_of_element(Register.go_to_login_user_page.select_user_account)
            self._click(Register.go_to_login_user_page.select_user_account)
            return self

    def open_register_page(self):
        with allure.step("Open the registration page"):
            self._click(Register.register_button)
            sleep(1)
            return self

    def fill_register_form(self, first_name, last_name, email, password):
        with allure.step('Fill registration form'):
            self._wait_for_clickable(Register.register_form.first_name)
            self._click(Register.register_form.first_name)
            self._input(Register.register_form.first_name, first_name)
            self._click(Register.register_form.last_name)
            self._input(Register.register_form.last_name, last_name)
            self._click(Register.register_form.email)
            self._input(Register.register_form.email, email)
            self._click(Register.register_form.password)
            self._input(Register.register_form.password, password)
            self._click(Register.register_form.confirm_password)
            self._input(Register.register_form.confirm_password, password)
            self._click(Register.register_form.register_button)
            sleep(1)
            return self

    def check_app_name(self):
        with allure.step('Check for "Blend_catalog" on the "applications_enduser" page'):
            self._wait_for_visibility_of_element(Register.app_name.app_name)
            assert 'Blend_Catalog' in self._get_element_text(Register.app_name.app_name), 'the widget name is not displayed'
            return self
