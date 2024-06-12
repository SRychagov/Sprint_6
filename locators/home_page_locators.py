from selenium.webdriver.common.by import By


class HomePageLocators:
    button_header_order = (By.XPATH, './/div[contains(@class, "Header_Nav")]/button[text()="Заказать"]')
    button_page_order = (By.XPATH, './/div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]')
    question = (By.XPATH, './/div[@id = "accordion__heading-{}"]')
    answer = (By.XPATH, './/div[@id="accordion__panel-{}"]/p')
    cookie = (By.ID, 'rcc-confirm-button')
    last_question = (By.XPATH, '(.//div[contains(@id,"accordion__heading-")])[last()]')
    logo_scooter = (By.XPATH, './/a[@href = "/"]')
    logo_yandex = (By.XPATH, './/a[@href = "//yandex.ru"]')
