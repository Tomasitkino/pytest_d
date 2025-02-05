import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure

class Vaucher_download_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    download_button = '//h2[contains(text(), ".pdf")]'

    # Getters

    def get_download_button(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.download_button)))

    # Actions
    def scroll_down(self, element):
        time.sleep(1)  # Немного ждем, чтобы прокрутка завершилась
        self.scroll_to_element(element)  # Прокручиваем элемент в центр экрана
        time.sleep(2)
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(element))  # Ожидаем кликабельность
        element.click()  # Кликаем по элементу

    def click_select_button(self):
        download_button = self.get_download_button()
        self.scroll_down(download_button)


    # Methods
    def vaucher_download_ticket(self):
        with allure.step('Скачать ваучер'):
            self.get_current_url()
            self.click_select_button()




