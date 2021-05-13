from page_objects import LoginPage
import pytest
import pickle
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Autorization with email')
@allure.feature('Autorization')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/ejfJaNJuagJ', "LINK", 'Video on what it looks like')
@pytest.mark.parametrize('execution_number', range(3))
@allure.description('''
In this test, we perform authorization via email.

Steps:
1) Select the type of account - User
2) Fill login form
3) Checking the correctness of opening the applications_enduser
4) Select and go to the application "Blend Catalog"
5) Checking the correctness of opening the application "Blend Catalog"
''')
def test_login_user(browser, execution_number):
    LoginPage(browser) \
        .login_user(email='qaubraine@gmail.com', password='Qatest1!') \
        .go_to_app() \
        .check_custom_text_widget()
    """"saving cookies in the file 'cookies.pkl' for further authorization"""
    pickle.dump(browser.get_cookies(), open('cookies.pkl', 'wb'))


@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Autorization with GitHub')
@allure.feature('Autorization')
@allure.story('with git')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/ejfJaNJuagJ', "LINK", 'Video on what it looks like')
@allure.description('''
In this test, we perform authorization via GitHub.

Steps:
1) Select the type of account - User
2) Select type of authorization - GitHab
3) Fill GitHab authorization form
4) Checking the correctness of opening the 'applications_enduser'
5) Select and go to the application "Blend Catalog"
6) Checking the correctness of opening the application "Blend Catalog"
''')

def test_login_user_github(browser):
    allure.attach.file('C:\\Users\\qaubr\\image.png', attachment_type=allure.attachment_type.PNG)
    LoginPage(browser) \
        .login_user_github(email='qaubraine@gmail.com', password='Runbox55w') \
        .go_to_app() \
        .check_custom_text_widget()


@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Autorization with GitLab')
@allure.feature('Autorization')
@allure.story('with git')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/ejfJaNJuagJ', "LINK", 'Video on what it looks like')
@allure.description('''
In this test, we perform authorization via GitLab.

Steps:
1) Select the type of account - User
2) Select type of authorization - GitLab
3) Fill GitLab authorization form
4) Checking the correctness of opening the 'applications_enduser'
5) Select and go to the application "Blend Catalog"
6) Checking the correctness of opening the application "Blend Catalog"
''')
@pytest.mark.skip
def test_login_user_gitlab(browser):
    LoginPage(browser) \
        .login_user_gitlab(email='anatoliy.olesh@ubraine.com', password='qJz3PfBN4mcNEazX') \
        .check_custom_text_widget()
