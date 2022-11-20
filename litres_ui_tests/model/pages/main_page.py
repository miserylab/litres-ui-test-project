from selene.support.shared import browser
import allure




class MainPage:

    def open(self, browser):
        with allure.step('Open main page'):
            browser.open('/')
            return self

    def search(self, value):
        browser.element("[name='q']").type(value)
        browser.element("[type='submit']").click()
        return self
