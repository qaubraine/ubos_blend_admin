class Register:
    register_button = {'css': '#kc-registration > span > a'}

    class go_to_login_user_page:
        select_user_account = {'xpath': '//*[@id="root"]/section/div/div/div/div/button[1]'}

    class register_form:

        first_name = {'css': '#firstName'}
        last_name = {'css': '#lastName'}
        email = {'css': '#email'}
        password = {'css': '#password'}
        confirm_password = {'css': '#password-confirm'}
        register_button = {'css': '#kc-form-buttons > input'}


    class app_name:
        app_name = {'css': '#root > div:nth-child(3) > div:nth-child(2) > div > div.sc-bwcZQD.eAnozt > span'}
