from selene import have
from selene.support.shared import browser
import allure


class LoginPage:

    def open(self, browser):
        with allure.step('Open login page'):
            browser.open('/pages/login/')
            return self

    def type_login(self, value):
        browser.element("[name='login']").type(value)
        return self

    def type_pwd(self, value):
        browser.element("#open_pwd_main").type(value)
        return self

    def click_login_button(self):
        browser.element('#login_btn').click()
        return self

    def check_profile_name(self, value):
        with allure.step('Check profile name after auth: test'):
            browser.element('.user_name').should(have.text(value))
            return self

    def check_error(self, value):
        with allure.step('Check error text: Login impossible (incorrect combination of login and password)'):
            browser.element('.err_text').should(have.text(value))
            return self


class LoginModal:

    def open(self, browser):
        with allure.step('Open login window'):
            browser.element("[href='/pages/login/']").hover().click()
            return self

    def check_is_opened(self, value):
        with allure.step('Check window is opened'):
            browser.element('.login-popup__head').should(have.text(value))
            return self

    def click_email_button(self):
        with allure.step('Click the "EMAIL ADDRESS" button'):
            browser.element('.btn_orange').click()
            return self

    def type_login(self, value):
        with allure.step('Type "EMAIL"'):
            browser.element("[name='email']").type(value)
            return self

    def click_resume_button(self):
        with allure.step('Click the "RESUME" button'):
            browser.element('.btn_orange').click()
            return self

    def type_pwd(self, value):
        with allure.step('Type "PASSWORD"'):
            browser.element("[name='pwd']").type(value)
            return self

    def click_login_button(self):
        with allure.step('Click the "LOG IN" button'):
            browser.element('.btn_orange').click()
            return self


class BackUpLogin:
    def close(self):
        with allure.step('Close back up login pop-up'):
            browser.element('.header-popup__login-popup .close').hover().click()
            return self
