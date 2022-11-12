__author__ = 'miserylab'
import allure
from litres_ui_tests.helpers import app


@allure.tag('ui')
@allure.epic('Search')
@allure.title('Test search(results exists)')
@allure.description('результаты существуют')
def test_check_about_us_top_section(setup_browser):

    with allure.step('Open about us page'):
        app.about_us_page.open()
    with allure.step('Check top title'):
        app.about_us_page.check_top_title('Passion for the best reading experience')
    with allure.step('Check top text'):
        app.about_us_page.check_top_text('LitRes is a convenient service that allows you to discover new books '
                                               'and read them on any platform, and every time you switch your reading '
                                               'device the book will open on the same page.')


