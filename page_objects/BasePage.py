from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def __element(self, selector: dict, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT

        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        return self.driver.find_element(by, selector)

    def _click(self, selector, link_text=None):
        self.__element(selector, link_text).click()

    def _input(self, selector, value):
        element = self.__element(selector)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, link_text=None, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, link_text)))

    def _get_element_text(self, selector):
        return self.__element(selector).text

    def _hover(self, selector):
        ActionChains(self.driver).move_to_element(self.__element(selector)).perform()

    def _switch_to_frame(self, selector):
        self.driver.switch_to.frame(self.__element(selector))

    def _switch_to_default(self):
        return self.driver.switch_to.default_content()

    def _select_dropdown(self, selector, value):
        select = Select(self.__element(selector))
        return select.select_by_value(value)

    def _wait_for_clickable(self, selector, link_text=None, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable(self.__element(selector, link_text)))

    def _wait_to_be_available_frame(self, selector, link_text=None, wait=10):
        return WebDriverWait(self.driver, wait).until(
            EC.frame_to_be_available_and_switch_to_it(self.__element(selector, link_text)))

    def _get_attribute_value(self, name_attribute, selector):
        return self.__element(selector).get_attribute(name_attribute)

    ################################################################################

    def __elements(self, selector: dict, index: int, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT

        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        return self.driver.find_elements(by, selector)[index]

    def _find_elements(self, selector: dict, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT

        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        return self.driver.find_elements(by, selector)

    def _click_elements(self, selector, index=0):
        self.__elements(selector, index).click()

    def _input_elements(self, selector, value, index=0):
        element = self.__elements(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible_elements(self, selector, link_text=None, index=0, wait=10):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__elements(selector, index, link_text)))

    def _get_element_text_elements(self, selector, index):
        return self.__elements(selector, index).text

    def _hover_elements(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.__elements(selector, index)).perform()

    def _switch_to_frame_elements(self, selector, index=0):
        self.driver.switch_to.frame(self.__elements(selector, index))

    def _select_dropdown_elements(self, selector, value, index=0):
        select = Select(self.__elements(selector, index))
        return select.select_by_value(value)

    def _wait_for_clickable_elements(self, selector, link_text=None, index=0, wait=10):
        return WebDriverWait(self.driver, wait).until(
            EC.element_to_be_clickable(self.__elements(selector, index, link_text)))

    def _wait_to_be_available_frame_elements(self, selector, link_text=None, wait=10, index=0):
        return WebDriverWait(self.driver, wait).until(
            EC.frame_to_be_available_and_switch_to_it(self.__elements(selector, index, link_text)))
