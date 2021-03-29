from page_objects import LoginPage
import pytest


@pytest.mark.parametrize('execution_number', range(1))
def test_login_user(browser, execution_number):
    LoginPage(browser) \
        .login_user(email='qaubraine@gmail.com', password='Qatest1!') \
        .go_to_app() \
        .check_app_name()


def test_login_user_github(browser):
    LoginPage(browser) \
        .login_user_github(email='qaubraine@gmail.com', password='Runbox55w') \
        .go_to_app() \
        .check_app_name()


@pytest.mark.skip
def test_login_user_gitlab(browser):
    LoginPage(browser) \
        .login_user_gitlab(email='anatoliy.olesh@ubraine.com', password='qJz3PfBN4mcNEazX') \
        .check_app_name()
