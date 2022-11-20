__author__ = 'miserylab'

import os
import allure
from litres_ui_tests.helpers import app
from dotenv import load_dotenv

load_dotenv()

WRONG_EMAIL = os.getenv('wrong_email')
EMAIL = os.getenv('email')
PASSWORD = os.getenv('password')


@allure.tag('ui')
@allure.epic('Authorization')
@allure.title('Test login on login page(positive)')
@allure.description('Пользователь существует в системе с введенным логином и паролем на странице авторизации')
def test_login_positive_on_login_page(setup_browser):
    browser = setup_browser

    app.login_page.open(browser)

    app.authorization()

    app.login_page.check_profile_name('test')


@allure.tag('ui')
@allure.epic('Authorization')
@allure.title('Test login in window(positive)')
@allure.description('Пользователь существует в системе с введенным логином и паролем в окне авторизации')
def test_login_positive_in_window(setup_browser):
    browser = setup_browser

    app.main_page.open(browser)

    app.login_modal.open(browser) \
        .check_is_opened('Log in or sign up') \
        .click_email_button() \
        .type_login(EMAIL) \
        .click_resume_button() \
        .type_pwd(PASSWORD) \
        .click_login_button()

    app.back_up_login_modal.close()

    app.login_page.check_profile_name('test')


@allure.tag('ui')
@allure.story('Authorization')
@allure.title('Test login with bad login(negative)')
@allure.description('Пользователь с введенным логином не существует в системе')
def test_login_negative_bad_login(setup_browser):
    browser = setup_browser

    app.login_page.open(browser)

    with allure.step('Authorization'):
        app.login_page.type_login(WRONG_EMAIL) \
            .type_pwd(PASSWORD) \
            .click_login_button()

    app.login_page.check_error('Login impossible (incorrect combination of login and password)')
