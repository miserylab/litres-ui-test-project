__author__ = 'miserylab'

from selene.support.shared import browser

class MainPage:

    def open(self):
        browser.open('/')
        return self

    def search(self, value):
        browser.element("[name='q']").type(value)
        browser.element("[type='submit']").click()
        return self


