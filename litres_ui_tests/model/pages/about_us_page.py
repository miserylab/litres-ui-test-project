from selene import have
from selene.support.shared import browser
import allure


class AboutUsPage:

    def open(self, browser):
        with allure.step('Open about us page'):
            browser.open('/about-us/')
            return self

    def check_top_title(self, value):
        with allure.step('Check top title'):
            browser.element(".aboutus-top__title").should(have.text(value))
            return self

    def check_top_text(self, value):
        with allure.step('Check top text'):
            browser.element(".aboutus-top__text").should(have.text(value))
            return self
