from selene.support.shared import browser
from selene import have
import allure

class SearchPage:

    def check_search_results(self, value):
        with allure.step('Check search results title: Search results for «Philip K. Dick»'):
            browser.element('.b_search h1').should(have.text(value))
            return self

    def check_number_of_books(self, value):
        with allure.step('Check number of books: 155'):
            browser.element('.item__type_author .result__type span').should(have.text(value))
            return self

    def check_author_name(self, value):
        with allure.step("Check author's name: Philip K. Dick"):
            browser.element('.result__name__href').should(have.text(value))
            return self

    def check_genres(self, value):
        browser.all('.result_book__list')[0].should(have.text(value))
        return self

    def check_the_best_books(self, value):
        browser.all('.result_book__list')[1].should(have.text(value))
        return self

    def not_found_result(self, value):
        browser.element('.ab-container h1').should(have.text(value))
        return self
