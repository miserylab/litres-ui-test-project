from selene import have
from selene.support.shared import browser


class AboutUsPage:

    def open(self, browser):
        browser.open('/about-us/')
        return self

    def check_top_title(self, value):
        browser.element(".aboutus-top__title").should(have.text(value))
        return self

    def check_top_text(self, value):
        browser.element(".aboutus-top__text").should(have.text(value))
        return self
