import os
from time import sleep
import pytest
import time
from selenium import webdriver
import allure


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="https://ubos.blend-dev.com/", help="choose your url")
    parser.addoption("--headless", action="store", default="true", help="Is headless driver? tru/false")


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def browser(request, url):
    headless = request.config.getoption("--headless")
    chrome_options = webdriver.ChromeOptions()
    if headless == "true":
        chrome_options.add_argument("headless")
    else:
        pass

    browser = request.config.getoption("--browser")
    """ To run UI tests in Gitlab CI"""
    chrome_options.add_argument('--disable-dev-shm-usage')
    if browser == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")

    # driver.implicitly_wait(10)
    request.addfinalizer(driver.close)
    driver.set_window_size(1920, 1080)

    def open(path=""):
        return driver.get(url + path)

    driver.open = open
    driver.open()
    return driver


@pytest.fixture()
def emails():
    emails = 'qaubraine+' + str(time.time()) + '@gmail.com'
    return emails

@pytest.fixture()
def current_time():
    current_time = str(time.time())
    return current_time

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:  # assume this is fixture with webdriver
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='Screenshot of the error page',
                attachment_type=allure.attachment_type.PNG
            )
            # if web_driver.browser_name != FIREFOX_BROWSER_NAME:
            #     # Firefox do not support js logs: https://github.com/SeleniumHQ/selenium/issues/2972
            #     allure.attach(
            #         '\n'.join(web_driver.get_log('browser')),
            #         name='js console log:',
            #         attachment_type=allure.attachment_type.TEXT,
            #     )

        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
