class Login:

    class go_to_login_user_page:
        select_user_account = {'css': '#root > section > div > div > div > div > button:nth-child(1)'}

    class user_login:
        email_field = {'css': '#username'}
        password_field = {'css': '#password'}
        login_button = {'css': '#kc-login'}


    class github_login:
        github_button = {'css': '#social-github'}
        email_github = {'css': '#login_field'}
        password_github = {'css': '#password'}
        sign_in_button = {'css': 'input[type=submit]'}
        autorize_spel = {'css': '#js-oauth-authorize-btn'}

    class gitlab_login:
        gitlab_button = {'css': '#social-gitlab'}
        email_gitlab = {'css': '#login_field'}
        password_gitlab = {'css': '#password'}
        sign_in_button = {'css': '#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block'}
        autorize_spel = {'css': '#js-oauth-authorize-btn'}

    class go_to_app:
        select_app = {'css': '#root > div:nth-child(3) > div:nth-child(2) > div > div'}
        launch_button = {'css': '#root > div:nth-child(3) > div:nth-child(2) > div > div div.overlay'}
