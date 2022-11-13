__author__ = 'miserylab'
import os
import allure
from litres_ui_tests.helpers import app
from dotenv import load_dotenv

load_dotenv()

NO_RESULTS = os.getenv('no_results')


@allure.tag('ui')
@allure.epic('Search')
@allure.title('Test search(results exists)')
@allure.description('результаты существуют')
def test_search_results_exists(setup_browser):
    browser = setup_browser
    with allure.step('Open main page'):
        app.main_page.open(browser)
    with allure.step('Type "Philip K. Dick" into the "search" field'):
        app.main_page.search('Philip K. Dick')
    with allure.step('Check results'):
        with allure.step('Check search results title: Search results for «Philip K. Dick»'):
            app.search_page.check_search_results('Search results for «Philip K. Dick»')
        with allure.step('Check number of books: 155'):
            app.search_page.check_number_of_books('155')
        with allure.step("Check author's name: Philip K. Dick"):
            app.search_page.check_author_name('Philip K. Dick')
        # with allure.step("Check author's genres"):
        #     app.search_page.check_genres('Writes in genres: Science fiction, Foreign fiction...')
        # with allure.step("Check author's best books"):
        #     app.search_page.check_the_best_books('The best books: The Science Fiction Anthology, The Science Fiction '
        #                                          'Anthology, Early Stories of Philip K. Dick, The Crystal Crypt ('
        #                                          'Unabridged)...')



@allure.tag('ui')
@allure.epic('Search')
@allure.title('Test search(results not exists)')
@allure.description('результаты не существуют + корректное сообщение о пустом результате')
def test_search_results_not_exists(setup_browser):
    browser = setup_browser
    with allure.step('Open main page'):
        app.main_page.open(browser)
    with allure.step(f'Type "{NO_RESULTS}" into the "search" field'):
        app.main_page.search(NO_RESULTS)
    with allure.step(f'Check results: By request «{NO_RESULTS}» Nothing found'):
        app.search_page.not_found_result(f'By request «{NO_RESULTS}» Nothing found')



