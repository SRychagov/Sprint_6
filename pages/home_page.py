import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from data import Urls


class HomePage(BasePage):
    @allure.step('Нажать на кнопку "Заказать" в хедере')
    def click_header_order_button(self):
        self.click_on_element(HomePageLocators.button_header_order)


    @allure.step('Нажать на кнопку "Заказать" на странице')
    def click_page_button(self):
        self.click_on_element(HomePageLocators.button_page_order)


    @allure.step('Нажать на вопрос')
    def click_question(self, number):
        method, locator = HomePageLocators.question
        locator = locator.format(number)
        return self.click_on_element((method, locator))


    @allure.step('Получить текст ответа на вопрос')
    def get_answer(self, number):
        method, locator = HomePageLocators.answer
        locator = locator.format(number)
        return self.get_text((method, locator))


    @allure.step('Открыть главную страницу "Яндекс Самокат"')
    def open_home_page(self):
        self.open_page(Urls.scooter_home_page)


    @allure.step('Нажать на лого "Яндекс"')
    def click_on_yandex_logo(self):
        self.click_on_element(HomePageLocators.logo_yandex)


    @allure.step('Нажать на лого "Самокат"')
    def click_on_scooter_logo(self):
        self.click_on_element(HomePageLocators.logo_scooter)


    @allure.step('Проверить URL "Яндекс Самокат"')
    def check_redirection_on_scooter_page(self):
        self.cross_url(Urls.scooter_home_page)


    @allure.step('Проверить URL "Дзен"')
    def check_redirection_on_dzen_page(self):
        self.cross_url(Urls.dzen_main_page)


    @allure.step('Принять куки')
    def accept_cookie(self):
        self.wait_element(HomePageLocators.cookie)
        self.click_on_element(HomePageLocators.cookie)


    @allure.step('Найти последний вопрос')
    def find_last_question(self):
        self.find_element(HomePageLocators.last_question)
