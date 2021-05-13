from page_objects import AdminPage, SearchFilter
import pytest
import allure


@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Check the opening of the main page")
@allure.feature('Admin Page')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.description('''
In this test, we check the opening of the main page.

Steps:
1) Open Admin Page
2) Checking the correct display of the product name 'קטלוג טמפו'
''')
@pytest.mark.parametrize('execution_number', range(3))
def test_open_home_page(browser, execution_number):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .check_custom_text_widget_ubos()


@allure.severity(allure.severity_level.NORMAL)
@allure.title('Go to the second page with the goods and return to the first')
@allure.feature('Admin Page')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.description('''
In this test, we check to go to the second page with the goods and return to the first.

Steps:
1) Open Admin Page
2) Go to the second page with the goods
3) Return to the first page
''')
def test_go_to_next_and_return_previous_page(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .go_to_next_previous_page(name_attribute='value')


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Search for a product by name")
@allure.feature('Search Product')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.description('''
In this test, we search for a product using its name.

Steps:
1) Open Admin Page
2) Enter the product name 'test' in the search field "name"
3) Click the 'Submit' button
4) Check that the found product is called 'test'
''')
def test_search_product_by_name(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_name(product_name='test') \
        .click_submit_button() \
        .check_name_found_product()


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Search for a product by SKU")
@allure.feature('Search Product')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.description('''
In this test, we search for a product using its SKU.

Steps:
1) Open Admin Page
2) Enter the product SKU '123' in the search field "SKU"
3) Click the 'Submit' button
4) Check that the found product has name 'test', and SKU '123'
''')
def test_search_product_by_sku(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='7002260') \
        .click_submit_button() \
        .check_name_found_product()


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Opening the form of creating a new product")
@allure.feature('Create Product')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.description('''
In this test we open the form of creating a new product.

Steps:
1) Open Admin Page
2) Click 'Create Product' button
3) Check what the name of the form is 'Create Product'
''')
def test_open_create_product_form(browser):
    AdminPage(browser) \
        .open_admin_page(browser) \
        .open_create_product_form()


@allure.severity(allure.severity_level.NORMAL)
@allure.title("Opening the product editing form")
@allure.feature('Edit Product')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.description('''
In this test we open the form of editing a product.

Steps:
1) Open Admin Page
2) Input product SKU
3) Click 'Submit button'
4) Check name found product
5) Opening Edit Product Form
6) Check what the name of the form is 'Edit Product'
7) 
''')
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
@allure.title('Changing the activity status of the product')
@allure.feature('Edit Product')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.description('''
In this test we changing the activity status of the product.

Steps:
1) Open Admin Page
2) Input product SKU
3) Click 'Submit button'
4) Check name found product
5) Opening Edit Product Form
6) Check what the name of the form is 'Edit Product'
7) Check current status the product
8) Change status the product
9) Close form
''')
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
@allure.title('Upload a picture in a folder "Image"')
@allure.feature('Edit Product')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.story('Image')
@allure.description('''
In this test we uploading a picture in a folder "Image".

Steps:
1) Open Admin Page
2) Input product SKU
3) Click 'Submit button'
4) Check name found product
5) Opening Edit Product Form
6) Check what the name of the form is 'Edit Product'
7) Click add image button
8) Select Image folder
9) Click Upload button
10) Selecting a image for upload
11) Check the display of the downloaded image in the list of available images
12) Close form
''')
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
@allure.title('Select a picture in a folder "Image"')
@allure.feature('Edit Product')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.story('Image')
@allure.description('''
In this test we selecting a picture in a folder "Image".

Steps:
1) Open Admin Page
2) Input product SKU
3) Click 'Submit button'
4) Check name found product
5) Opening Edit Product Form
6) Check what the name of the form is 'Edit Product'
7) Click add image button
8) Select Image folder
9) Check the display 'image.png' in the  image folder
10) Select "image.png" file
11) Check the display 'image.png' in the  image folder 
''')
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
@allure.title('Delete all images in a folder "Image"')
@allure.feature('Edit Product')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.story('Image')
@allure.description('''
In this test we deleting all images in a folder "Image".

Steps:
1) Open Admin Page
2) Input product SKU
3) Click 'Submit button'
4) Check name found product
5) Opening Edit Product Form
6) Check what the name of the form is 'Edit Product'
7) Click add image button
8) Select Image folder
9) Select all checkboxes
10) Click delete button
''')
def test_delete_images(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .delete_images()


@allure.severity(allure.severity_level.MINOR)
@allure.title('Upload a picture in a folder "Barcode"')
@allure.feature('Edit Product')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.story('Barcode')
@allure.description('''
In this test we uploading a picture in a folder "Barcode".

Steps:
1) Open Admin Page
2) Input product SKU
3) Click 'Submit button'
4) Check name found product
5) Opening Edit Product Form
6) Check what the name of the form is 'Edit Product'
7) Click add image button
8) Select Image folder
9) Click Upload button
10) Selecting a image for upload
11) Check the display of the downloaded image in the list of available images
12) Close form
''')
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


@allure.severity(allure.severity_level.MINOR)
@allure.title('Select a picture in a folder "Barcode"')
@allure.feature('Edit Product')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.story('Barcode')
@allure.description('''
In this test we selecting a picture in a folder "Barcode".

Steps:
1) Open Admin Page
2) Input product SKU
3) Click 'Submit button'
4) Check name found product
5) Opening Edit Product Form
6) Check what the name of the form is 'Edit Product'
7) Click add image button
8) Select Image folder
9) Check the display 'barcode.png' in the  image folder
10) Select "barcode.png" file
11) Check the display 'barcode.png' in the  image folder
''')
def test_select_bar_code_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .select_bar_code(value='value')


@allure.severity(allure.severity_level.MINOR)
@allure.title('Delete all images in a folder "Barcode"')
@allure.feature('Edit Product')
@allure.issue('https://ubraine.atlassian.net/secure/RapidBoard.jspa?rapidView=21&projectKey=BLEN', 'Task in Jira')
@allure.link('https://www.screencast.com/t/TiMV0wrXgcPY', "LINK", 'Video on what it looks like')
@allure.story('Barcode')
@allure.description('''
In this test we deleting all images in a folder "Barcode".

Steps:
1) Open Admin Page
2) Input product SKU
3) Click 'Submit button'
4) Check name found product
5) Opening Edit Product Form
6) Check what the name of the form is 'Edit Product'
7) Click add image button
8) Select Image folder
9) Select all checkboxes
10) Click delete button
''')
def test_delete_bar_code_product(browser):
    AdminPage(browser) \
        .open_admin_page(browser)
    SearchFilter(browser) \
        .input_product_sku(product_sku='123') \
        .click_submit_button() \
        .check_name_found_product()
    AdminPage(browser) \
        .delete_bar_code()
