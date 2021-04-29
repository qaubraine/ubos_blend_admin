from page_objects import LoginPage
import pytest
import pickle
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Autorization')
@allure.story('with email')
@pytest.mark.parametrize('execution_number', range(1))
def test_login_user(browser, execution_number):
    LoginPage(browser) \
        .login_user(email='qaubraine@gmail.com', password='Qatest1!') \
        .go_to_app() \
        .check_custom_text_widget()
    """"saving cookies in the file 'cookies.pkl' for further authorization"""
    pickle.dump(browser.get_cookies(), open('cookies.pkl', 'wb'))


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Autorization')
@allure.story('with gitHub')
def test_login_user_github(browser):
    LoginPage(browser) \
        .login_user_github(email='qaubraine@gmail.com', password='Runbox55w') \
        .go_to_app() \
        .check_custom_text_widget()


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Autorization')
@allure.story('with gitLab')
@pytest.mark.skip
def test_login_user_gitlab(browser):
    LoginPage(browser) \
        .login_user_gitlab(email='anatoliy.olesh@ubraine.com', password='qJz3PfBN4mcNEazX') \
        .check_custom_text_widget()
