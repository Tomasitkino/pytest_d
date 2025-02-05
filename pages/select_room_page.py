import random
import time
import datetime

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import re


class Select_room_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локатор кнопки "Забронировать" для всех элементов
    button_book_room_locator = '//button[@data-testid="btn-select-offer"]'
    room_locator = "//div[contains(@class, 'details')]"

    # Локатор для извлечения даты "Бесплатная отмена доступна до"
    cancellation_date_locator = "//p[contains(text(), 'Бесплатная отмена доступна до')]"

    # Получаем все кнопки "Забронировать"
    def get_all_book_room_buttons(self):
        # Получаем все кнопки с одинаковым локатором
        buttons = WebDriverWait(self.driver, 180).until(
            EC.presence_of_all_elements_located((By.XPATH, self.button_book_room_locator))
        )
        return buttons

        # Метод для проверки, что дата отмены позже текущей хотя бы на неделю

    def check_cancellation_date(self):
        try:
            # Извлекаем текст с фразы "Бесплатная отмена доступна до"
            cancellation_text = WebDriverWait(self.driver, 180).until(
                EC.presence_of_element_located((By.XPATH, self.cancellation_date_locator))
            ).text

            print(f"Текст, найденный с XPath: {cancellation_text}")

            # Регулярное выражение для извлечения даты в формате dd.mm.yyyy
            match = re.search(r'Бесплатная отмена доступна до\s*(\d{2}\.\d{2}\.\d{4})', cancellation_text)

            if match:
                date_str = match.group(1)
                print(f"Извлеченная дата: {date_str}")

                # Преобразуем строку в объект даты (без времени)
                try:
                    cancellation_date = datetime.datetime.strptime(date_str, "%d.%m.%Y")
                except ValueError:
                    print(f"Ошибка: не удалось преобразовать строку '{date_str}' в дату.")
                    return False

                # Получаем текущую дату
                current_date = datetime.datetime.now()

                # Проверяем, что дата отмены позже текущей хотя бы на неделю
                if cancellation_date > current_date + datetime.timedelta(weeks=1):
                    print(f"Дата отмены ({cancellation_date}) позже текущей даты на неделю.")
                    return True
                else:
                    print(f"Дата отмены ({cancellation_date}) слишком близка. Бронирование прекращено.")
                    return False
            else:
                print("Не удалось найти дату отмены в тексте.")
                return False

        except Exception as e:
            print("Ошибка при извлечении или сравнении даты отмены:", e)
            return False
    # Метод для выбора случайного номера (с прокруткой до него и проверки даты)
    def select_random_room(self):
        # Получаем все номера с кнопкой "Забронировать"
        rooms = WebDriverWait(self.driver, 180).until(
            EC.presence_of_all_elements_located((By.XPATH, self.room_locator))
        )

        if rooms:
            # Прокручиваем до случайного номера (не кликаем по нему)
            random_room = random.choice(rooms)
            self.scroll_to_element(random_room)

            # Проверяем дату отмены
            if not self.check_cancellation_date():
                print("Дата отмены слишком близка, бронирование прекращено.")
                return  # Прерываем выполнение, если дата отмены не удовлетворяет условиям

            # Если дата отмены удовлетворяет условиям, продолжаем выполнение теста
            print("Дата отмены подходящая, продолжаем выбор номера.")
            # Например, кликаем по кнопке "Забронировать"
            book_button = random_room.find_element(By.XPATH, ".//button[@data-testid='btn-select-offer']")
            book_button.click()

            time.sleep(2)
        else:
            print("Не удалось найти доступные номера.")

    def select_random_room_without_date_check(self):
        try:
            # Получаем все номера с кнопкой "Забронировать"
            rooms = WebDriverWait(self.driver, 180).until(
                EC.presence_of_all_elements_located((By.XPATH, self.room_locator))
            )

            if rooms:
                # Прокручиваем до случайного номера (не кликаем по нему)
                random_room = random.choice(rooms)
                self.scroll_to_element(random_room)

                # Печатаем, что будем продолжать выбор номера
                print("Дата отмены не проверяется, продолжаем выбор номера.")

                # Кликаем по кнопке "Забронировать"
                book_button = random_room.find_element(By.XPATH, ".//button[@data-testid='btn-select-offer']")
                book_button.click()

                time.sleep(2)  # Немного ждем, чтобы действие завершилось
            else:
                print("Не удалось найти доступные номера.")

        except Exception as e:
            print(f"Ошибка при выборе случайного номера: {e}")

    # Метод для прокрутки страницы до нужного элемента
    def scroll_to_element(self, element):
        # Прокручиваем элемент в видимую область с минимальной прокруткой
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'nearest'});", element)
        print(f"Элемент {element} прокручен в видимую область.")
        WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable(element))  # Ожидаем кликабельность
        time.sleep(2)

    # Метод для выбора случайного номера
    def select_random_room_action(self):
        with allure.step('Выбрать случайный номер'):
            self.get_current_url()  # Логируем текущий URL
            self.select_random_room_without_date_check()  # Выбираем случайный номер


# Метод для выбора случайного номера с логикой завершения теста
    def select_random_room_action_aa(self):
        with allure.step('Выбрать случайный номер'):
            self.get_current_url()  # Логируем текущий URД

            # Если дата отмены подходит, выбираем случайный номер
            self.select_random_room()

