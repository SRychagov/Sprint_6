import allure
from conftest import driver
from pages.home_page import HomePage
from data import Urls


class TestHeaderLogo:
    @allure.title('Клик на лого Самоката в шапке открывает главную страницу Яндекс Самокат')
    def test_redirect_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_header_order_button()
        home_page.click_on_scooter_logo()
        home_page.check_redirection_on_scooter_page()
        assert home_page.get_current_url() == Urls.scooter_home_page


    @allure.title('Клик на лого Яндекс в шапке открывает главную страницу Dzen')
    def test_redirect_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_on_yandex_logo()
        home_page.tab_switch(driver)
        home_page.check_redirection_on_dzen_page()
        assert home_page.get_current_url() == Urls.dzen_main_page
