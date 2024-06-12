from selenium.webdriver.common.by import By


class OrderPageLocators:
    field_name = (By.XPATH, './/input[@placeholder = "* Имя"]')
    field_last_name = (By.XPATH, './/input[@placeholder = "* Фамилия"]')
    field_address = (By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]')
    field_phone = (By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]')
    field_metro_station = (By.XPATH, './/input[@placeholder = "* Станция метро"]')
    station_metro = (By.XPATH, './/div[text() = "Сокольники"]')
    button_further = (By.XPATH, './/button[text() = "Далее"]')
    delivery_date_field = (By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]')
    date = (By.XPATH, './/div[@class = "react-datepicker__day react-datepicker__day--024"]')
    rental_period_field = (By.XPATH, './/div[@class = "Dropdown-placeholder"]')
    period = (By.XPATH, './/div[@class="Dropdown-option" and text()="сутки"]')
    color_scooter_grey = (By.XPATH, './/label[@for = "grey"]')
    field_comment = (By.XPATH, './/input[@placeholder = "Комментарий для курьера"]')
    button_order = (By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]')
    button_yes = By.XPATH, './/button[text() = "Да"]'
    popup_success = (By.XPATH, './/div[@class = "Order_Modal__YZ-d3"]')
