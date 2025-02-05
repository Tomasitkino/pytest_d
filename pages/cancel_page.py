# import json
# import time
#
# import requests
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from base.base_class import Base
# import allure
#
# class Cancel_page(Base):
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#
#     # locators
#
#     cancel_button = '//button[@data-testid="cancel-order-hotel"]'
#
#     # check cancelling
#     status_view = '//div[@class="h-6 px-2 py-1 rounded-xl bg-red-light text-red-dark text-xs leading-[133%] flex"]'
#
#     # Getters
#
#     def get_cancel_button(self):
#         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cancel_button)))
#
#     def get_status_view(self):
#         return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.status_view)))
#
#     # Actions
#     def click_cancel_button(self):
#         self.get_cancel_button().click()
#         print('Click cancel_button')
#
#     def get_order_id_from_url(self):
#         """Извлечь order_id из URL"""
#         WebDriverWait(self.driver, 10).until(
#             lambda driver: driver.current_url != self.get_current_url()  # Ждём изменения URL
#         )
#         current_url = self.get_current_url()
#         if current_url:
#             order_id = current_url.split("/")[-1]  # Разделяем URL и получаем последний элемент
#             print(f"Получен order_id: {order_id}")
#             return order_id
#         else:
#             print("Ошибка: не удалось получить текущий URL")
#             return None
#
#     # Methods
#     def cancel_order(self):
#         with allure.step('Отменить заказ'):
#             self.get_current_url()
#             self.click_cancel_button()
#             with allure.step('Статус заказа "отменен"'):
#                 status_view_element = self.get_status_view()
#                 self.scroll_to_element(status_view_element)
#                 self.assert_word_1(status_view_element, "Отменен")
#             with allure.step('Получить order_id'):
#                 self.get_order_id_from_url()



import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.api_cancel_page import Api_cancel_page  # Импортируем API-класс

class Cancel_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.api_cancel = Api_cancel_page()  # Инициализация API-класса

    # locators
    cancel_button = '//button[@data-testid="cancel-order-hotel"]'
    status_view = '//div[@class="h-6 px-2 py-1 rounded-xl bg-red-light text-red-dark text-xs leading-[133%] flex"]'

    # Getters
    def get_cancel_button(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.cancel_button)))

    def get_status_view(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.status_view)))

    # Actions
    def click_cancel_button(self):
        self.get_cancel_button().click()
        print('Click cancel_button')

    def get_order_id_from_url(self):
        """Извлечь order_id из URL"""
        WebDriverWait(self.driver, 180).until(
            lambda driver: driver.current_url != self.get_current_url()  # Ждём изменения URL
        )
        current_url = self.get_current_url()
        if current_url:
            order_id = current_url.split("/")[-1]  # Разделяем URL и получаем последний элемент
            print(f"Получен order_id: {order_id}")
            return order_id
        else:
            print("Ошибка: не удалось получить текущий URL")
            return None

    # Methods
    def cancel_order(self):
        with allure.step('Отменить заказ'):
            self.get_current_url()
            self.click_cancel_button()
            with allure.step('Статус заказа "отменен"'):
                status_view_element = self.get_status_view()
                self.scroll_to_element(status_view_element)
                self.assert_word_1(status_view_element, "Отменен")
            # with allure.step('Получить order_id'):
            #     order_id = self.get_order_id_from_url()
            #     if order_id:
            #         # Проверяем отмену через API
            #         api_cancel_result = self.api_cancel.cancel_booking(order_id)
            #         if api_cancel_result:
            #             print(f"Заказ с ID {order_id} успешно отменен через API.")
            #         else:
            #             print(f"Не удалось отменить заказ с ID {order_id} через API.")
            #     else:
            #         print("Не удалось получить order_id для последующей проверки через API.")









