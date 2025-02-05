import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

# for searching
text_client_1 = 'Д'

text_client_2 = 'Ста'


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    search_client = "//input[@data-testid='search-clients-all']"
    choose_client = "//div[@data-testid='suggestion-item-0']"

    # Getters

    def get_search_client(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.search_client)))

    def suggestion(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.choose_client)))

    # Actions

    # Searching by two items
    def input_search_client(self, search_client):
        with allure.step('Поиск клиента'):
            self.get_search_client().send_keys(search_client)
            print('Input name client')

    def click_client(self):
        with allure.step('Выбрать клиента'):
            self.suggestion().click()
            print('Click client')



    # Methods
    def choose_clients_1(self):
        with allure.step('Выбрать клиента Демонстрация(тестовые шлюзы)'):
            self.get_current_url()
            self.input_search_client(text_client_1)
            self.click_client()

    def choose_clients_prod(self):
        with allure.step('Выбрать Боевой шлюз'):
            self.get_current_url()
            self.input_search_client(text_client_2)
            self.click_client()




