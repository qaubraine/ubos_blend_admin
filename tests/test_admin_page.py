from page_objects import AdminPage, SearchFilter
import pytest


@pytest.mark.parametrize('execution_number', range(1))
def test_open_home_page(browser, execution_number):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .check_custom_text_widget_ubos()


def test_go_to_next_and_return_previous_page(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .go_to_next_previous_page(name_attribute='value')


def test_search_product_by_name(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_name(product_name='test') \
        .click_submit_button() \
        .check_name_found_product()


def test_search_product_by_sku(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()


def test_open_create_product_form(browser):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .open_create_product_form()


def test_edit_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .open_edit_form()


def test_change_status_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .change_status_product_activity()


def test_upload_image_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .upload_image(path='C:\\Users\\qaubr\\image.png') \
        .upload_image(path='C:\\Users\\qaubr\\bar_code.png')


def test_select_image_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .select_image(value='value')


def test_delete_images(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .delete_images()

def test_upload_bar_code_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .upload_bar_code(path='C:\\Users\\qaubr\\bar_code.png') \
        .upload_image(path='C:\\Users\\qaubr\\image.png')


def test_select_bar_code_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .select_bar_code(value='value')


def test_delete_bar_code_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .delete_bar_code()
