from page_objects import AdminPage, SearchFilter
import pytest
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Admin Page')
@allure.story('Check the opening of the main page')
@pytest.mark.parametrize('execution_number', range(1))
def test_open_home_page(browser, execution_number):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .check_custom_text_widget_ubos()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Admin Page')
@allure.story('Go to the second page with the goods and return to the first')
def test_go_to_next_and_return_previous_page(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .go_to_next_previous_page(name_attribute='value')


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Search Product')
@allure.story('Search for a product by name')
def test_search_product_by_name(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_name(product_name='test') \
        .click_submit_button() \
        .check_name_found_product()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Search Product')
@allure.story('Search for a product by serial number')
def test_search_product_by_sku(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Create Product')
@allure.story('Opening the form of creating a new product')
def test_open_create_product_form(browser):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .open_create_product_form()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Edit Product')
@allure.story('Opening the product editing form')
def test_edit_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .open_edit_form()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Edit Product')
@allure.story('Changing the activity status of the product')
def test_change_status_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .change_status_product_activity()


@allure.severity(allure.severity_level.MINOR)
@allure.feature('Edit Product')
@allure.story('Edit a picture in a folder "Image"')
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


@allure.severity(allure.severity_level.MINOR)
@allure.feature('Edit Product')
@allure.story('Select a picture in a folder "Image"')
def test_select_image_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .select_image(value='value')


@allure.severity(allure.severity_level.MINOR)
@allure.feature('Edit Product')
@allure.story('Delete a picture in a folder "Image"')
def test_delete_images(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .delete_images()


@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature('Edit Product')
@allure.story('Upload a picture in a folder "Barcode"')
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


@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature('Edit Product')
@allure.story('Select a picture in a folder "Barcode"')
def test_select_bar_code_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .select_bar_code(value='value')


@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature('Edit Product')
@allure.story('Delete a picture in a folder "Barcode"')
def test_delete_bar_code_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .delete_bar_code()
