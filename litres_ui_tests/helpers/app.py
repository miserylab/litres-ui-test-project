import os
from litres_ui_tests.model.pages.about_us_page import AboutUsPage
from litres_ui_tests.model.pages.login_page import LoginPage
from litres_ui_tests.model.pages.login_page import LoginModal
from litres_ui_tests.model.pages.login_page import BackUpLogin
from litres_ui_tests.model.pages.main_page import MainPage
from litres_ui_tests.model.pages.search_page import SearchPage
import allure

from dotenv import load_dotenv

about_us_page = AboutUsPage()
login_page = LoginPage()
login_modal = LoginModal()
main_page = MainPage()
back_up_login_modal = BackUpLogin()
search_page = SearchPage()

load_dotenv()

WRONG_EMAIL = os.getenv('wrong_email')
EMAIL = os.getenv('email')
PASSWORD = os.getenv('password')


def authorization():
    with allure.step('Authorization'):
        login_page.type_login(EMAIL)
        login_page.type_pwd(PASSWORD)
        login_page.click_login_button()


