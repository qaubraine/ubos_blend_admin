from locators import Admin
from .BasePage import BasePage
from time import sleep
import pickle


class AdminPage(BasePage):

    def open_admin_page(self, browser):
        """adding cookies for authorization from the cookie.pkl file"""
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            browser.add_cookie(cookie)
        """"go to the admin page. url + path"""
        browser.open(path='applications/605362b1cf12932736ef39c8/pages/605362b1cf12932736ef39ca')
        return self

    def check_custom_text_widget_ubos(self):
        self._wait_for_visibility_of_element(Admin.custom_text_widget.custom_text_widget_ubos)
        assert 'קטלוג טמפו' in self._get_element_text(Admin.custom_text_widget.custom_text_widget_ubos), \
            'The custom text widget is not displayed'
        return self

    def open_create_product_form(self):
        self._wait_for_clickable(Admin.create_product_button)
        self._click(Admin.create_product_button)
        self._wait_to_be_available_frame(Admin.iframe_create_product_form)
        self._wait_for_visibility_of_element(Admin.create_product_form.text_widget_create_form)
        assert 'Create Product' in self._get_element_text(Admin.create_product_form.text_widget_create_form), \
            'The create product form is not displayed'
        return self

    def open_edit_form(self):
        self._wait_for_clickable(Admin.edit_form_button)
        self._click(Admin.edit_form_button)
        self._wait_to_be_available_frame(Admin.iframe_edit_product_form)
        self._wait_for_visibility_of_element(Admin.edit_product_form.text_widget_edit_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        return self

    def change_status_product_activity(self):
        self._wait_for_clickable(Admin.edit_form_button)
        self._click(Admin.edit_form_button)
        self._wait_to_be_available_frame(Admin.iframe_edit_product_form)
        self._wait_for_visibility_of_element(Admin.edit_product_form.text_widget_edit_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        self._wait_for_visibility_of_element(Admin.edit_product_form.click_drop_down)
        if self._get_element_text(Admin.edit_product_form.status_field) == 'public':
            self._wait_for_clickable(Admin.edit_product_form.click_drop_down)
            self._click(Admin.edit_product_form.click_drop_down)
            self._wait_for_clickable(Admin.edit_product_form.status_draft)
            self._click(Admin.edit_product_form.status_draft)
        else:
            self._click(Admin.edit_product_form.click_drop_down)
            self._wait_for_clickable(Admin.edit_product_form.status_public)
            self._click(Admin.edit_product_form.status_public)
        self._wait_for_clickable(Admin.edit_product_form.submit_button)
        self._click(Admin.edit_product_form.submit_button)
        self._switch_to_default()
        self._wait_for_clickable(Admin.edit_product_form.close_form_button)
        self._click(Admin.edit_product_form.close_form_button)
        return self

    def upload_image(self, path):
        image_names = []
        self._wait_for_clickable(Admin.edit_form_button)
        self._click(Admin.edit_form_button)
        self._wait_to_be_available_frame(Admin.iframe_edit_product_form)
        self._wait_for_visibility_of_element(Admin.edit_product_form.text_widget_edit_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        self._wait_for_clickable(Admin.edit_product_form.image.add_image_button)
        self._click(Admin.edit_product_form.image.add_image_button)
        self._wait_for_clickable(Admin.edit_product_form.image.select_folder_image)
        self._click(Admin.edit_product_form.image.select_folder_image)
        self._wait_for_clickable(Admin.edit_product_form.image.upload_button_image)
        self._click(Admin.edit_product_form.image.upload_button_image)
        self._wait_for_visibility_of_element(Admin.edit_product_form.image.choose_file_image)
        self._input(Admin.edit_product_form.image.choose_file_image, path)
        self._wait_for_clickable(Admin.edit_product_form.image.ok_button_image)
        self._click(Admin.edit_product_form.image.ok_button_image)
        self._wait_for_visibility_of_all_elements(Admin.edit_product_form.image_name)
        image_list = (self._find_elements(Admin.edit_product_form.image_name))
        for i in image_list:
            image_names.append(i.text)
        assert 'image.png' in image_names, 'The name of the uploaded file is not displayed'
        self._switch_to_default()
        self._click(Admin.edit_product_form.close_form_button)
        return self

    def select_image(self, value):
        self._wait_for_clickable(Admin.edit_form_button)
        self._click(Admin.edit_form_button)
        self._wait_to_be_available_frame(Admin.iframe_edit_product_form)
        self._wait_for_visibility_of_element(Admin.edit_product_form.text_widget_edit_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        self._wait_for_clickable(Admin.edit_product_form.image.add_image_button)
        self._click(Admin.edit_product_form.image.add_image_button)
        self._wait_for_clickable(Admin.edit_product_form.image.select_folder_image)
        self._click(Admin.edit_product_form.image.select_folder_image)
        self._wait_for_visibility_of_element(Admin.edit_product_form.image.image_png)
        assert self._find_elements(Admin.edit_product_form.image.image_png), 'The test file "image.png" not found'
        self._click(Admin.edit_product_form.image.image_png)
        self._wait_for_visibility_of_element(Admin.edit_product_form.image.image_path)
        assert 'image/image.png' in self._get_attribute_value(value, Admin.edit_product_form.image.image_path), \
            'Unexpected file path'
        self._click(Admin.edit_product_form.submit_button)
        self._wait_for_visibility_of_element(Admin.edit_product_form.product_update_message)
        assert 'Product Update' in self._get_element_text(Admin.edit_product_form.product_update_message), \
            '"Product Update" message not displayed'

    def delete_images(self):
        self._wait_for_clickable(Admin.edit_form_button)
        self._click(Admin.edit_form_button)
        self._wait_to_be_available_frame(Admin.iframe_edit_product_form)
        self._wait_for_visibility_of_element(Admin.edit_product_form.text_widget_edit_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        self._wait_for_clickable(Admin.edit_product_form.image.add_image_button)
        self._click(Admin.edit_product_form.image.add_image_button)
        self._wait_for_clickable(Admin.edit_product_form.image.select_folder_image)
        self._click(Admin.edit_product_form.image.select_folder_image)
        sleep(1)
        all_checkboxes = self._find_elements(Admin.edit_product_form.checkbox_field)
        checkboxes = all_checkboxes[1:]
        for checkbox in checkboxes:
            checkbox.click()
        self._wait_for_clickable(Admin.edit_product_form.delete_button)
        self._click(Admin.edit_product_form.delete_button)

    def upload_bar_code(self, path):
        bar_code_names = []
        self._wait_for_clickable(Admin.edit_form_button)
        self._click(Admin.edit_form_button)
        self._wait_to_be_available_frame(Admin.iframe_edit_product_form)
        self._wait_for_visibility_of_element(Admin.edit_product_form.text_widget_edit_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        self._wait_for_clickable(Admin.edit_product_form.barcode.add_bar_code_button)
        self._click(Admin.edit_product_form.barcode.add_bar_code_button)
        self._wait_for_clickable(Admin.edit_product_form.barcode.select_folder_bar_code)
        self._click(Admin.edit_product_form.barcode.select_folder_bar_code)
        self._wait_for_clickable(Admin.edit_product_form.barcode.upload_button_barcode)
        self._click(Admin.edit_product_form.barcode.upload_button_barcode)
        self._wait_for_visibility_of_element(Admin.edit_product_form.barcode.choose_file_bar_code)
        self._input(Admin.edit_product_form.barcode.choose_file_bar_code, path)
        self._wait_for_clickable(Admin.edit_product_form.barcode.ok_button_bar_code)
        self._click(Admin.edit_product_form.barcode.ok_button_bar_code)
        self._wait_for_visibility_of_all_elements(Admin.edit_product_form.image_name)
        image_list = (self._find_elements(Admin.edit_product_form.image_name))
        for i in image_list:
            bar_code_names.append(i.text)
        assert 'bar_code.png' in bar_code_names, 'The name of the uploaded file is not displayed'
        self._switch_to_default()
        self._click(Admin.edit_product_form.close_form_button)
        return self

    def select_bar_code(self, value):
        self._wait_for_clickable(Admin.edit_form_button)
        self._click(Admin.edit_form_button)
        self._wait_to_be_available_frame(Admin.iframe_edit_product_form)
        self._wait_for_visibility_of_element(Admin.edit_product_form.text_widget_edit_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        self._wait_for_clickable(Admin.edit_product_form.barcode.add_bar_code_button)
        self._click(Admin.edit_product_form.barcode.add_bar_code_button)
        self._wait_for_clickable(Admin.edit_product_form.barcode.select_folder_bar_code)
        self._click(Admin.edit_product_form.barcode.select_folder_bar_code)
        self._wait_for_visibility_of_element(Admin.edit_product_form.barcode.bar_code_png)
        assert self._find_elements(Admin.edit_product_form.barcode.bar_code_png), \
            'The test file "bar_code.png" not found'
        self._wait_for_clickable(Admin.edit_product_form.barcode.bar_code_png)
        self._click(Admin.edit_product_form.barcode.bar_code_png)
        self._wait_for_visibility_of_element(Admin.edit_product_form.barcode.bar_code_path)
        assert 'bar_code.png' in self._get_attribute_value(value, Admin.edit_product_form.barcode.bar_code_path), \
            'Unexpected file path'
        self._click(Admin.edit_product_form.submit_button)
        self._wait_for_visibility_of_element(Admin.edit_product_form.product_update_message)
        assert 'Product Update' in self._get_element_text(Admin.edit_product_form.product_update_message), \
            '"Product Update" message not displayed'

    def delete_bar_code(self):
        self._wait_for_clickable(Admin.edit_form_button)
        self._click(Admin.edit_form_button)
        self._wait_to_be_available_frame(Admin.iframe_edit_product_form)
        self._wait_for_visibility_of_element(Admin.edit_product_form.text_widget_edit_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        self._wait_for_clickable(Admin.edit_product_form.barcode.add_bar_code_button)
        self._click(Admin.edit_product_form.barcode.add_bar_code_button)
        self._wait_for_clickable(Admin.edit_product_form.barcode.select_folder_bar_code)
        self._click(Admin.edit_product_form.barcode.select_folder_bar_code)
        sleep(1)
        all_checkboxes = self._find_elements(Admin.edit_product_form.checkbox_field)
        checkboxes = all_checkboxes[1:]
        for checkbox in checkboxes:
            checkbox.click()
        self._wait_for_clickable(Admin.edit_product_form.delete_button)
        self._click(Admin.edit_product_form.delete_button)
