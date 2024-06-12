import pytest
import allure
from conftest import driver
from pages.home_page import HomePage
from data import PageFAQ


class TestFAQ:
    @allure.title('Проверка соответсвия вопрос-ответ из выпадающего списка "Вопросы о важном"')
    @pytest.mark.parametrize('number, answer', PageFAQ.answers)
    def test_faq(self, driver, number, answer):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.accept_cookie()
        home_page.find_last_question()
        home_page.click_question(number)
        assert home_page.get_answer(number) == answer
