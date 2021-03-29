from page_objects import RegisterPage
import pickle


def test_register_user(browser, emails):
    RegisterPage(browser) \
        .open_login_page() \
        .open_register_page() \
        .fill_register_form(first_name='Anatolii', last_name='Olesh', email=emails,
                            password='Qatest1!') \
        .check_app_name()
    """"saving cookies in the file 'cookies.pkl' for further authorization"""
    pickle.dump(browser.get_cookies(), open('cookies.pkl', 'wb'))
