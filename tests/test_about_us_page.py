import allure
from litres_ui_tests.helpers import app


@allure.tag('ui')
@allure.title('Test the "About Us" page')
def test_check_about_us_top_section(setup_browser):
    browser = setup_browser

    app.about_us_page.open(browser) \
        .check_top_title('Passion for the best reading experience') \
        .check_top_text('LitRes is a convenient service that allows you to discover new books '
                        'and read them on any platform, and every time you switch your reading '
                        'device the book will open on the same page.')

