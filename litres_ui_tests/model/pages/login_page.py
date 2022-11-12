from selene import have
from selene.support.shared import browser


class LoginPage:

    def open(self):
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
        browser.element('.user_name').should(have.text(value))
        return self

    def check_error(self, value):
        browser.element('.err_text').should(have.text(value))
        return self

class LoginModal:

    def open(self):
        browser.element("[href='/pages/login/']").hover().click()
        return self

    def check_is_opened(self, value):
        browser.element('.login-popup__head').should(have.text(value))
        return self

    def click_email_button(self):
        browser.element('.btn_orange').click()
        return self

    def type_login(self, value):
        browser.element("[name='email']").type(value)
        return self

    def click_resume_button(self):
        browser.element('.btn_orange').click()
        return self

    def type_pwd(self, value):
        browser.element("[name='pwd']").type(value)
        return self

    def click_login_button(self):
        browser.element('.btn_orange').click()


class BackUpLogin:
    def close(self):
        browser.element('.header-popup__login-popup .close').hover().click()