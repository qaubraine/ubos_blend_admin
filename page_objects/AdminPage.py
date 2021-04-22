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
        assert 'קטלוג טמפו' in self._get_element_text(Admin.custom_text_widget.custom_text_widget_ubos), \
            'The custom text widget is not displayed'
        sleep(1)
        return self

    def open_create_product_form(self):
        self._click(Admin.create_product_button)
        self._switch_to_frame(Admin.iframe_create_product_form)
        assert 'Create Product' in self._get_element_text(Admin.create_product_form.text_widget_create_form), \
            'The create product form is not displayed'
        return self

    def open_edit_form(self):
        self._click(Admin.edit_form_button)
        self._switch_to_frame(Admin.iframe_edit_product_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        return self

    def change_status_product_activity(self):
        self._click(Admin.edit_form_button)
        self._switch_to_frame(Admin.iframe_edit_product_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        sleep(1)
        if self._get_element_text(Admin.edit_product_form.status_field) == 'public':
            self._click(Admin.edit_product_form.click_drop_down)
            self._click(Admin.edit_product_form.status_draft)
        else:
            self._click(Admin.edit_product_form.click_drop_down)
            self._click(Admin.edit_product_form.status_public)
        self._click(Admin.edit_product_form.submit_button)
        self._switch_to_default()
        self._click(Admin.edit_product_form.close_form_button)
        return self

    def upload_image(self, path):
        image_names = []
        self._click(Admin.edit_form_button)
        self._switch_to_frame(Admin.iframe_edit_product_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        sleep(1)
        self._click(Admin.edit_product_form.add_image_button)
        self._click(Admin.edit_product_form.select_folder_image)
        self._click(Admin.edit_product_form.upload_button_image)
        self._input(Admin.edit_product_form.choose_file_image, path)
        self._click(Admin.edit_product_form.ok_button_image)
        image_list = (self._find_elements(Admin.edit_product_form.image_name))
        for i in image_list:
            image_names.append(i.text)
        assert 'image.png' in image_names, 'The name of the uploaded file is not displayed'
        self._switch_to_default()
        self._click(Admin.edit_product_form.close_form_button)
        return self


    def select_image(self, name):
        self._click(Admin.edit_form_button)
        self._switch_to_frame(Admin.iframe_edit_product_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        sleep(1)
        self._click(Admin.edit_product_form.add_image_button)
        self._click(Admin.edit_product_form.select_folder_image)
        sleep(1)
        self._wait_for_visible(name, link_text=True)
        self._click(Admin.edit_product_form.image_png)
        sleep(5)




    def upload_bar_code(self, path):
        bar_code_names = []
        self._click(Admin.edit_form_button)
        self._switch_to_frame(Admin.iframe_edit_product_form)
        assert 'Edit Product' in self._get_element_text(Admin.edit_product_form.text_widget_edit_form), \
            'The edit product form is not displayed'
        sleep(1)
        self._click(Admin.edit_product_form.add_bar_code_button)
        self._click(Admin.edit_product_form.select_folder_bar_code)
        self._click(Admin.edit_product_form.upload_button_barcode)
        self._input(Admin.edit_product_form.choose_file_bar_code, path)
        self._click(Admin.edit_product_form.ok_button_bar_code)
        image_list = (self._find_elements(Admin.edit_product_form.image_name))
        for i in image_list:
            bar_code_names.append(i.text)
        assert 'bar_code.png' in bar_code_names, 'The name of the uploaded file is not displayed'
        self._switch_to_default()
        self._click(Admin.edit_product_form.close_form_button)
        return self
