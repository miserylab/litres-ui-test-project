__author__ = 'miserylab'

import allure
import pytest
from selene import have
from selene.support.shared import browser


@pytest.mark.positive
@allure.tag('ui')
@allure.epic('Authorization')
@allure.title('Test login on login page(positive)')
@allure.description('Пользователь существует в системе с введенным логином и паролем на странице авторизации')
def test_login_positive_on_login_page():
    with allure.step('Open login page'):
        browser.open('/pages/login/')
    with allure.step('Authorization'):
        browser.element("[name='login']").type('miserylab.r6s@gmail.com')
        browser.element('#open_pwd_main').type('akcyig3h')
        browser.element('#login_btn').click()
    with allure.step('Check profile name after auth'):
        browser.element('.Profile-module__name').should(have.text('test'))

@pytest.mark.positive
@allure.tag('ui')
@allure.epic('Authorization')
@allure.title('Test login in window(positive)')
@allure.description('Пользователь существует в системе с введенным логином и паролем в окне авторизации')
def test_login_positive_in_window():
    with allure.step('Open main page'):
        browser.open('/')
    with allure.step('Open login window'):
        browser.element("[href='/pages/login/']").hover().click()
        browser.element('.ButtonV1-module__button__orange').click()
        browser.element("[name='email']").type('miserylab.r6s@gmail.com')
        browser.element(".ButtonV1-module__button__orange").click()
        browser.element("[name='pwd']").type('akcyig3h')

@pytest.mark.negative
@allure.tag('ui')
@allure.story('Authorization')
@allure.title('Test login with bad login(negative)')
@allure.description('Пользователь с введенным логином не существует в системе')
def test_login_negative_bad_login():
    with allure.step('Open login page'):
        browser.open('/pages/login/')
    with allure.step('Authorization'):
        browser.element("[name='login']").type('miserylab.r6s@gmail.co')
        browser.element('#open_pwd_main').type('akcyig3h')
        browser.element('#login_btn').click()
    with allure.step('Check error text'):
        browser.element('.err_text').should(have.text('Логин невозможен (неверное сочетание логина и пароля)'))


# @allure.tag('ui')
# @allure.story('Authorization')
# @allure.title('Test login with bad password(negative)')
# @allure.description('Пользователь с введенным логином существует в системе, но пароль неверный')
# def test_login_negative_bad_password():
#     with step('Open login page'):
#         browser.open('/pages/login/')
#     with step('Authorization'):
#         browser.element("[name='login']").type('miserylab.r6s@gmail.com')
#         browser.element('#open_pwd_main').type('111')
#         browser.element('#login_btn').click()
#     with step('Check error text'):
#         browser.element('.err_text').should(have.text('Логин невозможен (неверное сочетание логина и пароля)'))


