import random
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Search_hotel_page(Base):

    # Локаторы
    search_town = '//input[@data-testid="city-search-hotels"]'  # Поле ввода для поиска города
    select_town = "//div[@data-testid='city-suggestion-0']"  # Локатор для первого города в саджестере
    date_check_in = "//input[@id='datepicker-заезд']"  # Локатор для поля даты заезда
    date_check_out = "//input[@id='datepicker-выезд']"  # Локатор для поля даты выезда
    search_button = "//button[text()='Найти']"  # Локатор кнопки поиска
    number_of_guests = "//button[@data-testid='guests-btn-search-hotels']" #локатор кнопки количство гостей
    two_guests = "//input[@data-testid='guests-two']"

    # Получатели для элементов
    def get_search_town(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.search_town)))

    def get_select_town(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.select_town)))

    def get_date_check_in(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.date_check_in)))

    def get_date_check_out(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.date_check_out)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_number_of_guests(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.number_of_guests)))

    def get_two_guests(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.two_guests)))

    # Метод для генерации случайной даты
    def generate_random_date(self, start_date, max_date, days_range=(1, 28)):
        """
        Генерирует случайную дату начиная с start_date и до max_date.
        Учитывает переданный диапазон дней для выборки.
        """
        # Разница в днях между start_date и max_date
        delta_days = (max_date - start_date).days
        if delta_days <= 0:
            raise ValueError("max_date должна быть позже start_date")

        # Генерируем случайное количество дней от start_date в пределах delta_days
        random_days = random.randint(days_range[0], min(days_range[1], delta_days))
        random_date = start_date + timedelta(days=random_days)

        # Форматируем дату в строку
        return random_date, random_date.strftime('%d %B %Y')  # Пример: '01 Января 2025'

    # Метод для выбора случайных дат
    def random_select_check_in_out(self):
        # Получаем сегодняшнюю дату
        today = datetime.today()

        # Дата заезда будет минимум через 2 недели от сегодняшней
        min_check_in_date = today + timedelta(weeks=2)

        # Дата заезда не может быть позже чем через 6 месяцев от текущей даты
        max_check_in_date = today + timedelta(weeks=26)  # 6 месяцев

        # Генерируем случайную дату заезда
        check_in_date, check_in_str = self.generate_random_date(min_check_in_date, max_check_in_date)

        # Дата выезда минимум через 1 день от заезда
        max_check_out_date = check_in_date + timedelta(weeks=26)  # максимальный выезд через 6 месяцев от заезда
        check_out_date = check_in_date + timedelta(days=random.randint(1, 7))  # Выезд минимум через 1 день
        check_out_str = check_out_date.strftime('%d %B %Y')

        # Логируем сгенерированные даты
        print(f"Сгенерированная дата заезда: {check_in_str}")
        print(f"Сгенерированная дата выезда: {check_out_str}")

        # Вводим даты в соответствующие поля на странице
        self.get_date_check_in().clear()  # Очищаем поле ввода
        self.get_date_check_in().send_keys(check_in_str)  # Вводим дату заезда

        self.get_date_check_out().clear()  # Очищаем поле ввода
        self.get_date_check_out().send_keys(check_out_str)  # Вводим дату выезда

        return check_in_str, check_out_str

    # метод для АА
    def random_select_check_in_out_AA(self):

        # Получаем сегодняшнюю дату
        today = datetime.today()

        # Дата заезда будет минимум через 2 недели от сегодняшней
        min_check_in_date = today + timedelta(weeks=27)

        # Дата заезда не может быть позже чем через 6 месяцев от текущей даты
        max_check_in_date = today + timedelta(weeks=52)  # 6 месяцев

        # Генерируем случайную дату заезда
        check_in_date, check_in_str = self.generate_random_date(min_check_in_date, max_check_in_date)

        # Дата выезда минимум через 1 день от заезда
        max_check_out_date = check_in_date + timedelta(weeks=2)  # максимальный выезд через 6 месяцев от заезда
        check_out_date = check_in_date + timedelta(days=random.randint(1, 7))  # Выезд минимум через 1 день
        check_out_str = check_out_date.strftime('%d %B %Y')

        # Логируем сгенерированные даты
        print(f"Сгенерированная дата заезда: {check_in_str}")
        print(f"Сгенерированная дата выезда: {check_out_str}")

        # Вводим даты в соответствующие поля на странице
        self.get_date_check_in().clear()  # Очищаем поле ввода
        self.get_date_check_in().send_keys(check_in_str)  # Вводим дату заезда

        self.get_date_check_out().clear()  # Очищаем поле ввода
        self.get_date_check_out().send_keys(check_out_str)  # Вводим дату выезда

        return check_in_str, check_out_str

    # Действия
    def input_search_town(self, search_town):
        with allure.step('Поиск города'):
            self.get_search_town().send_keys(search_town)  # Вводим название города
            print(f"Город {search_town} введен в поле поиска.")

    def click_select_town(self):
        with allure.step('Выбор города из саджестера'):
            self.get_select_town().click()  # Выбираем первый город из саджестера
            print('Город выбран из выпадающего списка.')

    def click_search_button(self):
        with allure.step('Нажать кнопку "Найти"'):
            self.get_search_button().click()  # Нажимаем кнопку поиска
            print('Нажата кнопка "Найти"')


    def click_number_of_guests(self):
        with allure.step('Нажать кнопку "Найти"'):
            self.get_number_of_guests().click()  # Нажимаем кнопку поиска
            print('Нажата кнопка "Найти"')

    def click_two_guests(self):
        with allure.step('Нажать кнопку "Найти"'):
            self.get_two_guests().click()  # Нажимаем кнопку поиска
            print('Нажата кнопка "Найти"')

    # Методы для поиска отелей с случайными датами
    def search_hotel_with_random_dates(self, town_name):
        with allure.step(f'Поиск отеля для города: {town_name}'):
            self.get_current_url()  # Проверяем текущий URL, чтобы убедиться, что находимся на нужной странице
            self.input_search_town(town_name)  # Вводим город в поле поиска
            self.click_select_town()  # Выбираем город из саджестера

            # Выбираем случайные даты заезда и выезда
            check_in_str, check_out_str = self.random_select_check_in_out()

            # Нажимаем кнопку поиска
            self.click_search_button()

            # Логируем сгенерированные данные
            print(f"Поиск отеля с датами: заезд {check_in_str}, выезд {check_out_str}")


    # Методы для поиска отелей с случайными датами
    def search_hotel_with_random_dates_two_guests(self, town_name):
        with allure.step(f'Поиск отеля для города: {town_name}'):
            self.get_current_url()  # Проверяем текущий URL, чтобы убедиться, что находимся на нужной странице
            self.input_search_town(town_name)  # Вводим город в поле поиска
            self.click_select_town()  # Выбираем город из саджестера

            # Выбираем случайные даты заезда и выезда
            check_in_str, check_out_str = self.random_select_check_in_out()

            # Выбираем двух гостей
            self.click_number_of_guests()
            self.click_two_guests()

            # Нажимаем кнопку поиска
            self.click_search_button()

            # Логируем сгенерированные данные
            print(f"Поиск отеля с датами: заезд {check_in_str}, выезд {check_out_str}")

    # метод для АА

    def search_hotel_with_random_dates_AA(self, town_name):
        with allure.step(f'Поиск отеля для города: {town_name}'):
            self.get_current_url()  # Проверяем текущий URL, чтобы убедиться, что находимся на нужной странице
            self.input_search_town(town_name)  # Вводим город в поле поиска
            self.click_select_town()  # Выбираем город из саджестера

            # Выбираем случайные даты заезда и выезда
            check_in_str, check_out_str = self.random_select_check_in_out_AA()

            # Нажимаем кнопку поиска
            self.click_search_button()

            # Логируем сгенерированные данные
            print(f"Поиск отеля с датами: заезд {check_in_str}, выезд {check_out_str}")

    # Пример тестов с случайными датами
    def search_hotel_1(self):
        self.search_hotel_with_random_dates('Ек')

    def search_hotel_2(self):
        self.search_hotel_with_random_dates('Соч')

    def search_hotel_3(self):
        self.search_hotel_with_random_dates('Москва')

    def search_hotel_4(self):
        self.search_hotel_with_random_dates('Москва')

    def search_hotel_AA(self):
        self.search_hotel_with_random_dates_AA('Москва')

    def search_hotel_two_guests(self):
        self.search_hotel_with_random_dates_two_guests('Москва')

    def search_hotel_two_guests_sochi(self):
        self.search_hotel_with_random_dates_two_guests('Сочи')


    def search_hotel_two_guests_tver(self):
        self.search_hotel_with_random_dates_two_guests('Тверь')











