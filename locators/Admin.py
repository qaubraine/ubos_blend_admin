class Admin:

    name_found_product = {'css': '#tablewdw2uan7zx > div.tableWrap > div > div.tbody.no-scroll > div:nth-child(1) > div:nth-child(2) > div'}
    create_product_button = {'css': 'div.appsmith_widget_1k94pt83a6 > div > div > div > button'}
    iframe_create_product_form = {'css': '#h5gqytssfl > div > iframe'}
    edit_form_button = {'css': '#tablewdw2uan7zx > div.tableWrap > div > div.tbody > div:nth-child(1) > div:nth-child(11) > div > div > button'}
    iframe_edit_product_form = {'css': '#gy0nb83vpl > div > iframe'}


    class custom_text_widget:
        custom_text_widget_ubos = {'css': 'div.appsmith_widget_s5vslteyis  > div > div > div > div > span'}
        ubraine_logo = {'css': '#root > header > div.sc-kGVuQl.dlbFmD > a > img'}
        blend_catalog = {'css': '#root > div:nth-child(3) > div:nth-child(2) > div > div.sc-bwcZQD.eAnozt > span'}

    class create_product_form:
        text_widget_create_form = {'css': '#roydb21ksg > div > div > div > div > span'}

    class edit_product_form:
        text_widget_edit_form = {'css': '#jdh2ip9xmk > div > div > div > div > span'}
        status_field = {'css': '#r95vmnofe5 > div > div > div > div > span > span > div > button > span.bp3-button-text'}
        click_drop_down = {'css': '#r95vmnofe5 > div > div > div > div > span > span > div > button > span.bp3-icon.bp3-icon-chevron-down'}
        status_draft = {'css': 'body > div.bp3-portal > div > div > div > div > div > ul > li:nth-child(2) > a > div'}
        status_public = {'css': 'body > div.bp3-portal > div > div > div > div > div > ul > li:nth-child(3) > a > div'}
        submit_button = {'css': '#ll1ryo6nty > div > div > div > button'}
        close_form_button = {'css': '#\\35gf5hxwj3m > div > div > div > div > div > div'}
        delete_button = {'css': 'button.button.delete_button.false'}
        image_name = {'css': 'tr > td:nth-child(3) > span'}
        product_update_message = {'css': '#root > div.Toastify > div > div > div > div'}
        checkbox_field = {'css': 'input[type="checkbox"]'}

        class image:
            add_image_button = {'css': '#xbwsjti1fr > div > div > div > div > div > div'}
            select_folder_image = {'css': '#ttjsj5j5qm > div > div > div > div.table_wrapper > table > tbody > tr:nth-child(3) > td:nth-child(3) > span'}
            upload_button_image = {'css': '#ttjsj5j5qm > div > div > div > div.topHeader > div:nth-child(2) > button'}
            choose_file_image = {'css': '#ttjsj5j5qm > div > div > div > div.wrapper_rename_modal > div > div:nth-child(2) > label > input[type=file]'}
            ok_button_image = {'css': '#ttjsj5j5qm > div > div > div > div.wrapper_rename_modal > div > div.wrapper_button > button'}
            iframe_select_image_form = {'css': '#gy0nb83vpl > div > iframe'}
            image_png = {'xpath': '//*[contains(text(), "image.png")]'}
            image_path = {'css': '#m60oig6nzq > div > div > div > div > span > span > div > input'}

        class barcode:
            add_bar_code_button = {'css': '#\\36 nws9v4lvh > div > div > div > div > div > div'}
            select_folder_bar_code = {'css': '#qdz0629ppx > div > div > div > div.table_wrapper > table > tbody > tr:nth-child(2) > td:nth-child(3)'}
            upload_button_barcode = {'css': '#qdz0629ppx > div > div > div > div.topHeader > div:nth-child(2) > button'}
            choose_file_bar_code = {'css': '#qdz0629ppx > div > div > div > div.wrapper_rename_modal > div > div:nth-child(2) > label > input[type=file]'}
            ok_button_bar_code = {'css': '#qdz0629ppx > div > div > div > div.wrapper_rename_modal > div > div.wrapper_button > button'}

            bar_code_png = {'xpath': '//*[contains(text(), "bar_code.png")]'}
            bar_code_path = {'css': '#\\33 b8w1fcnfi > div > div > div > div > span > span > div > input'}

