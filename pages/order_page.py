import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        self.send_keys(OrderPageLocators.field_name, name)


    @allure.step('Заполнить поле "Фамилия"')
    def set_last_name(self, last_name):
        self.send_keys(OrderPageLocators.field_last_name, last_name)


    @allure.step('Заполнить поле "Адрес: куда привезти заказ"')
    def set_address(self, address):
        self.send_keys(OrderPageLocators.field_address, address)


    @allure.step('Выбрать станцию метро')
    def set_metro(self, station_metro):
        self.click_on_element(OrderPageLocators.field_metro_station)
        self.click_on_element(station_metro)


    @allure.step('Заполнить поле "Телефон: на него позвонит курьер"')
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.field_phone, phone)


    @allure.step('Нажать на кнопку "Далее"')
    def click_further_button(self):
        self.click_on_element(OrderPageLocators.button_further)


    @allure.step('Выбрать дату доставки')
    def set_date(self, date):
        self.click_on_element(OrderPageLocators.delivery_date_field)
        self.click_on_element(date)


    @allure.step('Выбрать срок аренды')
    def set_period(self, period):
        self.click_on_element(OrderPageLocators.rental_period_field)
        self.click_on_element(period)


    @allure.step('Выбрать цвет')
    def set_color(self, color):
        self.click_on_element(color)


    @allure.step('Заполнить поле "Комментарий для курьера"')
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.field_comment, comment)


    @allure.step('Проверить появление модального окна "Заказ оформлен"')
    def check_success_order(self):
        return self.get_text(OrderPageLocators.popup_success)


    @allure.step('Нажать на кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.button_order)


    @allure.step('Нажать на кнопку "Да"')
    def click_yes_button(self):
        self.click_on_element(OrderPageLocators.button_yes)


    @allure.step('Оформить заказ')
    def create_order(self, user):
        self.set_name(user['name'])
        self.set_last_name(user['last_name'])
        self.set_address(user['address'])
        self.set_metro(OrderPageLocators.station_metro)
        self.set_phone(user['phone'])
        self.click_further_button()
        self.set_date(OrderPageLocators.date)
        self.set_period(OrderPageLocators.period)
        self.set_color(OrderPageLocators.color_scooter_grey)
        self.set_comment(user['comment'])
        self.click_order_button()
        self.click_yes_button()
