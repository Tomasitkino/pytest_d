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
# import requests
# import pytest
# import json
#
# import requests
#
# import requests
# import json
#
# import requests
# import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class Api_cancel_page:
#     BASE_URL = "http://158.160.116.223"
#     LOGIN_URL = "http://158.160.116.223/auth/login"
#     DEM_LINK_URL = f"{BASE_URL}/orders"
#     BRONEVIK_URL = f"{BASE_URL}/stays/bronevik"
#
#     login = "manager_vasiliy"
#     password = "yh5KKwpYIvizhGw"
#
#     def __init__(self):
#         self.token = None
#         self.order_ext_id = None
#         # Инициализация драйвера
#
#     def get_auth_token(self):
#         """Получить токен авторизации"""
#         json_new_location = {
#             "login": self.login,
#             "password": self.password
#         }
#
#         headers = {
#             "Content-Type": "application/json"
#         }
#
#         try:
#             print("Отправляем запрос на получение токена...")
#             print(f"URL запроса: {self.LOGIN_URL}")
#             print(f"Данные запроса: {json.dumps(json_new_location, indent=2)}")
#
#             response = requests.post(self.LOGIN_URL, json=json_new_location, headers=headers)
#
#             print(f"Ответ от сервера: {response.status_code} - {response.text}")
#
#             # Дополнительные проверки ответа
#             if response.status_code == 200:
#                 json_response = response.json()
#                 if json_response.get("Status") == "Success":
#                     self.token = json_response.get("Token")
#                     print("Токен успешно получен:", self.token)
#                     return self.token
#                 else:
#                     print(f"Ошибка: Статус не 'Success'. Ответ: {json_response}")
#                     return None
#             else:
#                 print(f"Ошибка: Неверный статус ответа. Код: {response.status_code}")
#                 return None
#
#         except requests.exceptions.RequestException as e:
#             print(f"Ошибка при получении токена: {e}")
#             return None
#
#     def _send_get_request(self, url, headers):
#         """Универсальный метод для отправки GET-запросов с токеном"""
#         try:
#             response = requests.get(url, headers=headers)
#             response.raise_for_status()  # Поднимет исключение при ошибке статуса
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             print(f"Ошибка при выполнении запроса {url}: {e}")
#             return None
#
#     def _send_delete_request(self, url, headers):
#         """Отправка DELETE-запроса для отмены бронирования"""
#         try:
#             response = requests.delete(url, headers=headers)
#             response.raise_for_status()  # Поднимет исключение при ошибке статуса
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             print(f"Ошибка при отмене бронирования через {url}: {e}")
#             return None
#
#
#     def get_order_ext_id(self, order_id):
#         """Получить order_ext_id для конкретного заказа"""
#         if not self.token:
#             print("Ошибка: Токен не был получен")
#             return None
#
#         headers = {
#             "Authorization": f"Bearer {self.token}"
#         }
#
#         # Получаем данные о заказе
#         order_data = self._send_get_request(f"{self.DEM_LINK_URL}/{order_id}", headers)
#         if order_data:
#             self.order_ext_id = order_data.get("order_ext_id")
#             return self.order_ext_id
#         else:
#             print(f"Не удалось получить данные для ордера {order_id}")
#             return None
#
#     def cancel_booking(self, order_id):
#         """Отмена бронирования через API"""
#         if not self.token:
#             print("Ошибка: Токен не был получен")
#             return False
#
#         # Извлекаем order_ext_id
#         order_ext_id = self.get_order_ext_id(order_id)
#         if not order_ext_id:
#             print(f"Не удалось получить order_ext_id для заказа {order_id}")
#             return False
#
#         headers = {
#             "Authorization": f"Bearer {self.token}"
#         }
#
#         # URL для отмены бронирования
#         cancel_url = f"{self.BRONEVIK_URL}/{order_ext_id}/cancel"
#         print(f"Отправляем запрос на отмену бронирования. URL: {cancel_url}")
#
#         # Отправляем запрос на отмену бронирования
#         cancel_response = self._send_delete_request(cancel_url, headers)
#         if cancel_response:
#             status = cancel_response.get("status")
#             if status == "Cancelled":
#                 print(f"Бронирование {order_id} успешно отменено")
#                 return True
#             else:
#                 print(f"Не удалось отменить бронирование {order_id}. Статус: {status}")
#                 return False
#         else:
#             print(f"Ошибка при отмене бронирования для {order_id}")
#             return False




import requests
import json

class Api_cancel_page:
    BASE_URL = "http://158.160.116.223"
    LOGIN_URL = "http://158.160.116.223/auth/login"
    DEM_LINK_URL = f"{BASE_URL}/orders"
    BRONEVIK_URL = f"{BASE_URL}/stays/bronevik"
    login = "manager_vasiliy"
    password = "yh5KKwpYIvizhGw"

    def __init__(self):
        self.token = None
        self.order_ext_id = None

    def get_auth_token(self):
        """Получить токен авторизации"""
        json_new_location = {
            "login": self.login,
            "password": self.password
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            print("Отправляем запрос на получение токена...")
            response = requests.post(self.LOGIN_URL, json=json_new_location, headers=headers)
            if response.status_code == 200:
                json_response = response.json()
                if json_response.get("Status") == "Success":
                    self.token = json_response.get("Token")
                    print("Токен успешно получен:", self.token)
                    return self.token
                else:
                    print(f"Ошибка: Статус не 'Success'. Ответ: {json_response}")
                    return None
            else:
                print(f"Ошибка: Неверный статус ответа. Код: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении токена: {e}")
            return None

    def _send_get_request(self, url, headers):
        """Универсальный метод для отправки GET-запросов с токеном"""
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Поднимет исключение при ошибке статуса
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса {url}: {e}")
            return None

    def _send_delete_request(self, url, headers):
        """Отправка DELETE-запроса для отмены бронирования"""
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()  # Поднимет исключение при ошибке статуса
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при отмене бронирования через {url}: {e}")
            return None

    def get_order_ext_id(self, order_id):
        """Получить order_ext_id для конкретного заказа"""
        if not self.token:
            print("Ошибка: Токен не был получен")
            return None

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        # Получаем данные о заказе
        order_data = self._send_get_request(f"{self.DEM_LINK_URL}/{order_id}", headers)
        if order_data:
            self.order_ext_id = order_data.get("order_ext_id")
            return self.order_ext_id
        else:
            print(f"Не удалось получить данные для ордера {order_id}")
            return None

    def cancel_booking(self, order_id):
        """Отмена бронирования через API"""
        if not self.token:
            print("Ошибка: Токен не был получен")
            return False

        # Извлекаем order_ext_id
        order_ext_id = self.get_order_ext_id(order_id)
        if not order_ext_id:
            print(f"Не удалось получить order_ext_id для заказа {order_id}")
            return False

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        # URL для отмены бронирования
        cancel_url = f"{self.BRONEVIK_URL}/{order_ext_id}/cancel"
        print(f"Отправляем запрос на отмену бронирования. URL: {cancel_url}")

        # Отправляем запрос на отмену бронирования
        cancel_response = self._send_delete_request(cancel_url, headers)
        if cancel_response:
            status = cancel_response.get("status")
            if status == "Cancelled":
                print(f"Бронирование {order_id} успешно отменено")
                return True
            else:
                print(f"Не удалось отменить бронирование {order_id}. Статус: {status}")
                return False
        else:
            print(f"Ошибка при отмене бронирования для {order_id}")
            return False



