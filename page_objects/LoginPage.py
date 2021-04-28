from selenium.common.exceptions import NoSuchElementException
from locators import Login, Admin
from .BasePage import BasePage
from time import sleep


class LoginPage(BasePage):

    def login_user(self, email, password):
        self._wait_for_visibility_of_element(Login.go_to_login_user_page.select_user_account)
        self._click(Login.go_to_login_user_page.select_user_account)
        self._wait_for_visibility_of_element(Login.user_login.email_field)
        self._input(Login.user_login.email_field, email)
        self._input(Login.user_login.password_field, password)
        self._click(Login.user_login.login_button)
        self._wait_for_visibility_of_element(Admin.custom_text_widget.blend_catalog)
        assert 'Blend_Catalog' in self._get_element_text(Admin.custom_text_widget.blend_catalog), \
            'Blend_catalog  widget is not presented '
        return self

    def go_to_app(self):
        self._wait_for_visibility_of_element(Login.go_to_app.select_app)
        self._hover(Login.go_to_app.select_app)
        self._click(Login.go_to_app.launch_button)
        return self

    def check_custom_text_widget(self):
        self._wait_for_visibility_of_element(Admin.custom_text_widget.custom_text_widget_ubos)
        assert 'קטלוג טמפו' in self._get_element_text(Admin.custom_text_widget.custom_text_widget_ubos),\
            'The custom text wiget is not displayed'
        return self

    def login_user_github(self, email, password):
        self._wait_for_clickable(Login.go_to_login_user_page.select_user_account)
        self._click(Login.go_to_login_user_page.select_user_account)
        self._click(Login.github_login.github_button)
        self._wait_for_clickable(Login.github_login.email_github)
        self._input(Login.github_login.email_github, email)
        self._input(Login.github_login.password_github, password)
        self._click(Login.github_login.sign_in_button)
        sleep(1)
        try:
            self._click(Login.github_login.autorize_spel)
        except NoSuchElementException:
            pass
        self._wait_for_visibility_of_element(Admin.custom_text_widget.ubraine_logo)
        assert 'Blend_Catalog' in self._get_element_text(Admin.custom_text_widget.blend_catalog), \
            'Blend_catalog  widget is not presented '
        return self

    def login_user_gitlab(self, email, password):
        self._wait_for_clickable(Login.go_to_login_user_page.select_user_account)
        self._click(Login.go_to_login_user_page.select_user_account)
        self._click(Login.gitlab_login.gitlab_button)
        self._wait_for_visibility_of_element(Login.gitlab_login.email_gitlab)
        self._input(Login.gitlab_login.email_gitlab, email)
        self._input(Login.gitlab_login.password_gitlab, password)
        self._click(Login.gitlab_login.sign_in_button)
        self._wait_for_visibility_of_element(Admin.custom_text_widget.ubraine_logo)
        assert 'Blend_Catalog' in self._get_element_text(Admin.custom_text_widget.blend_catalog), \
            'Blend_catalog  widget is not presented '
        return self
