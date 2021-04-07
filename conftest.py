import pytest
import time
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="https://app.ubos.tech/", help="choose your url")
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

    driver.implicitly_wait(10)
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
