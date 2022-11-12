__author__ = 'miserylab'

import os
import allure
import pytest
from litres_ui_tests.helpers import app
from dotenv import load_dotenv

load_dotenv()

WRONG_EMAIL = os.getenv('wrong_email')
EMAIL = os.getenv('email')
PASSWORD = os.getenv('password')


@pytest.mark.positive
@allure.tag('ui')
@allure.epic('Authorization')
@allure.title('Test login on login page(positive)')
@allure.description('Пользователь существует в системе с введенным логином и паролем на странице авторизации')
def test_login_positive_on_login_page(setup_browser):
    browser = setup_browser

    with allure.step('Open login page'):
        app.login_page.open()
    with allure.step('Authorization'):
        app.authorization()
    with allure.step('Check profile name after auth'):
        app.login_page.check_profile_name('test')


@pytest.mark.positive
@allure.tag('ui')
@allure.epic('Authorization')
@allure.title('Test login in window(positive)')
@allure.description('Пользователь существует в системе с введенным логином и паролем в окне авторизации')
def test_login_positive_in_window(setup_browser):
    browser = setup_browser
    with allure.step('Open main page'):
        app.main_page.open()
    with allure.step('Open login window'):
        app.login_modal.open()
    with allure.step('Check window is opened'):
        app.login_modal.check_is_opened('Log in or sign up')

    with allure.step('Click the "EMAIL ADDRESS" button'):
        app.login_modal.click_email_button()

    with allure.step('Type "EMAIL"'):
        app.login_modal.type_login(EMAIL)

    with allure.step('Click the "RESUME" button'):
        app.login_modal.click_resume_button()

    with allure.step('Type "PASSWORD"'):
        app.login_modal.type_pwd(PASSWORD)
    with allure.step('Click the "LOG IN" button'):
        app.login_modal.click_login_button()

    with allure.step('Close back up login pop-up'):
        app.back_up_login_modal.close()

    with allure.step('Check profile name after auth'):
        app.login_page.check_profile_name('test')

@pytest.mark.negative
@allure.tag('ui')
@allure.story('Authorization')
@allure.title('Test login with bad login(negative)')
@allure.description('Пользователь с введенным логином не существует в системе')
def test_login_negative_bad_login(setup_browser):
    browser = setup_browser
    with allure.step('Open login page'):
        app.login_page.open()
    with allure.step('Authorization'):
        app.login_page.type_login(WRONG_EMAIL)
        app.login_page.type_pwd(PASSWORD)
        app.login_page.click_login_button()
    with allure.step('Check error text'):
        app.login_page.check_error('Login impossible (incorrect combination of login and password)')
