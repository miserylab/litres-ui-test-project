__author__ = 'miserylab'

import allure
from selene import have
from selene.support.shared import browser


@allure.tag('ui')
@allure.epic('Search')
@allure.title('Test search(results exists)')
@allure.description('результаты существуют')
def test_search_results_exists():
    with allure.step('Open main page'):
        browser.open('/')
    with allure.step('Type search values'):
        browser.element("[name='q']").type('Филип Дик')
        browser.element("[type='submit']").click()
    with allure.step('Check results'):
        browser.element('.SearchTitle-module__title_YEbWG').should(have.text('Результаты поиска «Филип Дик»'))
        browser.element('.Person-module__personInfo_2wHPo .Person-module__numberOfBooks_2JkR1').should(have.text('Автор — 168 книг'))
        browser.element('.Person-module__personInfo_2wHPo .Person-module__title_1IJh3').should(have.text('Филип'))
        browser.element('.Person-module__personInfo_2wHPo .Person-module__title_1IJh3').should(have.text('Дик'))


@allure.tag('ui')
@allure.epic('Search')
@allure.title('Test search(results not exists)')
@allure.description('результаты не существуют + корректное сообщение о пустом результате')
def test_search_results_not_exists():
    with allure.step('Open main page'):
        browser.open('/')
    with allure.step('Type search values'):
        browser.element("[name='q']").type('1111111111111111111111')
        browser.element("[type='submit']").click()
    with allure.step('Check results'):
        browser.element('.SearchTitle-module__title__empty_horcZ').should(have.text('Ничего не найдено'))
        browser.element('.SearchTitle-module__subtitle__empty_3-hJs').should(have.text('Попробуйте изменить запрос'))



