from page_objects import RegisterPage
import pytest
import allure


@allure.severity(allure.severity_level.MINOR)
@allure.title('Registration using email')
@allure.feature('Registration')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.description('''
In this test we registration using email.

Steps:
1) Select the type of account - User
2) Open the registration page
3) Fill registration form
4) Check for "Blend_catalog" on the "applications_enduser" page
''')
@pytest.mark.skip
def test_register_user(browser, emails):
    RegisterPage(browser) \
        .open_login_page() \
        .open_register_page() \
        .fill_register_form(first_name='Anatolii', last_name='Olesh', email=emails,
                            password='Qatest1!') \
        .check_app_name()

