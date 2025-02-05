import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from base.base_class import Base

import random
import time


class Filter_hotel_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    type_hotel_button_1 = "(//div[@class='item flex justify-between text-sm items-center text-black-100']//input[@type='checkbox'])[1]"
    type_hotel_button_2 = "(//div[@class='item flex justify-between text-sm items-center text-black-100']//input[@type='checkbox'])[2]"
    type_hotel_text_2 = "(//div[@class='checkbox-holder']//div[contains(@class, 'item')])[2]//label[@class='text-gray-700 font-light select-none cursor-pointer mt-px']//span[contains(text(), '')]"
    choose_stars_0 = '//div[@data-testid="0-star"]'
    choose_stars_2 = '//div[@data-testid="2-star"]'
    cost_period_filter = '//input[@data-testid="cost-period"]'
    sort_high_cost = '//input[@data-testid="sorting-high-price"]'
    hotel_type_elements_locator = '//div[@class="h-6 px-2.5 py-1 rounded-xl bg-black-05 flex items-center text-xs text-nowrap"]'
    hotel_checkbox_locator = "//div[contains(@class, 'custom-checkbox')]//input[@type='checkbox']"
    hotel_stars_locator = "//div[@class='stars-content flex font-inter p-4 pl-3 text-sm flex-wrap']//div[contains(@class, 'star-checkbox')]"
    hotel_stars_result = "//h2[@class='name-stars font-nekst uppercase font-semibold text-[22px] leading-[109%]']"
    hotel_cost_locator = "//div[@class='radio-content flex flex-col font-inter p-4 pl-3 text-sm' and @data-testid='cost-block']//input[@data-testid='cost-night']"
    initial_price_elements = "//h2[@class='price text-[28px] leading-[114%] font-semibold']"




    # Getters
    def get_type_hotel_button_1(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.type_hotel_button_1))
        )

    def get_type_hotel_button_2(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.type_hotel_button_2))
        )

    def get_hotel_type_elements_locator(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.hotel_type_elements_locator))
        )

    def get_hotel_stars_locator(self):
        return WebDriverWait(self.driver, 180).until(
            EC.presence_of_all_elements_located((By.XPATH, self.hotel_stars_locator))
        )

    def get_type_hotel_text_2(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.type_hotel_text_2))
        )

    def get_choose_stars_0(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_stars_0))
        )

    def get_choose_stars_2(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_stars_2))
        )

    def get_cost_period_filter(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.cost_period_filter))
        )

    def get_sort_high_cost(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.sort_high_cost))
        )

    def get_hotel_cost_locator(self):
        return WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, self.hotel_cost_locator))
        )

    def get_initial_price(self):
        return WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, self.initial_price_elements))
        )

    def get_filtered_price(self):
        return WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, self.initial_price_elements))
        )

    # Actions
    def click_cost_filter(self):
        # Находим элемент фильтра стоимости
        cost_filter = WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.hotel_cost_locator))
        )

        # Прокручиваем до элемента
        self.scroll_to_element(cost_filter)

        # Кликаем по фильтру
        cost_filter.click()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'nearest'});", element)
        print(f"Элемент {element} прокручен в видимую область.")
        time.sleep(2)
        WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable(element))

    # Actions

    def click_random_hotel_checkbox(self):

        # Печатаем все элементы, которые мы пытаемся найти
        checkboxes = WebDriverWait(self.driver, 180).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class, 'custom-checkbox')]//input[@type='checkbox']"))
        )

        # Проверяем, что чекбоксы найдены
        if checkboxes:
            print(f"Найдено {len(checkboxes)} чекбоксов.")
            # Выбираем случайный чекбокс
            random_checkbox = random.choice(checkboxes)

            # Находим соответствующий текст рядом с выбранным чекбоксом
            try:
                checkbox_text = random_checkbox.find_element(By.XPATH, "following::label[1]//span//p//span").text
                print(f"Текст рядом с чекбоксом: {checkbox_text}")
            except Exception as e:
                print(f"Ошибка при извлечении текста: {e}")
                checkbox_text = None

            # Прокручиваем до чекбокса и кликаем
            self.scroll_to_element(random_checkbox)
            random_checkbox.click()
            print(f"Клик по случайному чекбоксу с текстом: {checkbox_text}")



            # Возвращаем текст для дальнейшего использования, если нужно
            return checkbox_text
        else:
            print("Чекбоксы не найдены.")
            return None

    def click_random_star(self):
        """
        Кликает по случайной звезде в фильтре и возвращает её текст.
        """
        # Получаем все элементы звезд
        stars_elements = self.get_hotel_stars_locator()

        # Проверяем, что элементы звезд найдены
        if stars_elements:
            print(f"Найдено {len(stars_elements)} типов звезд.")
            # Выбираем случайную звезду
            random_star = random.choice(stars_elements)

            # Извлекаем текст с выбранной звезды
            try:
                star_text = random_star.text.strip()
                print(f"Текст выбранной звезды: {star_text}")
            except Exception as e:
                print(f"Ошибка при извлечении текста: {e}")
                star_text = None

                # Если текст на кнопке "Без звезд", возвращаем "0"
            if star_text == "Без звезд":
                star_text = "0"
                print(f"Текст на кнопке 'Без звезд', устанавливаем значение: {star_text}")

            # Прокручиваем до элемента и кликаем
            self.scroll_to_element(random_star)
            random_star.click()
            print(f"Клик по случайной звезде с текстом: {star_text}")

            # Возвращаем текст для дальнейшего использования, если нужно
            return star_text
        else:
            print("Элементы звезд не найдены.")
            return None

    def check_filtered_hotel_stars(self):
        """
        Проверяет, что все отели в выдаче соответствуют выбранному фильтру по звездам.
        Сравниваем текст из случайно выбранной звезды с текстами, отображающимися на странице в карточках отелей.
        """
        # Шаг 1: Кликаем по случайной звезде и извлекаем текст рядом с ней
        selected_star = self.click_random_star()  # Возвращает текст выбранной звезды
        if selected_star is None:
            print("Не удалось получить текст из звезды.")
            return

        print(f"Выбранная звезда: {selected_star}")

        # Шаг 2: Получаем все тексты звезд, которые отображаются на странице в карточках отелей
        hotel_stars_on_page = self.driver.find_elements(By.XPATH, self.hotel_stars_result)

        # Преобразуем список в массив текстов
        hotel_stars_texts = [hotel_star.text.strip() for hotel_star in hotel_stars_on_page]

        # Шаг 3: Проверяем, что все тексты на странице соответствуют выбранному фильтру
        for hotel_star_text in hotel_stars_texts:
            assert selected_star in hotel_star_text, f"Текст '{selected_star}' не найден в '{hotel_star_text}'"

        print("Все отели соответствуют выбранному фильтру по звездам.")
    def check_filtered_hotel_types(self):
        """
        Проверяет, что все отели в выдаче соответствуют выбранному фильтру.
        Сравниваем текст из случайно выбранного чекбокса с текстами, отображающимися на странице в карточках отелей.
        """
        # Шаг 1: Кликнуть по случайному чекбоксу и извлечь текст рядом с ним
        selected_type = self.click_random_hotel_checkbox()  # Возвращает текст рядом с чекбоксом
        if selected_type is None:
            print("Не удалось получить текст из чекбокса.")
            return

        print(f"Выбранный тип размещения: {selected_type}")

        # Шаг 2: Получаем все тексты типов размещений, которые отображаются на странице в карточках отелей
        hotel_types_on_page = self.driver.find_elements(By.XPATH, self.hotel_type_elements_locator)

        # Преобразуем список в массив текстов
        hotel_types_texts = [hotel_type.text for hotel_type in hotel_types_on_page]

        # Шаг 3: Проверяем, что все тексты на странице соответствуют выбранному фильтру
        for hotel_type_text in hotel_types_texts:
            assert selected_type in hotel_type_text, f"Текст '{selected_type}' не найден в '{hotel_type_text}'"

        print("Все отели соответствуют выбранному фильтру.")



    def get_first_element_text(self, locator):
        """
        Функция для получения текста первого элемента по локатору.
        Если элемент найден, возвращает его текст, иначе None.
        """
        try:
            # Прокручиваем страницу до элемента, если нужно
            self.scroll_to_element(locator)

            # Ожидаем появления хотя бы одного элемента с данным локатором
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
            return element.text.strip()  # Извлекаем текст первого элемента
        except Exception as e:
            print(f"Элемент по локатору '{locator}' не найден: {e}")
            return None

    def click_element(self, locator):
        """
        Функция для клика по элементу, который найден по локатору.
        Если элемент найден, выполняет клик.
        """
        try:
            # Прокручиваем страницу до элемента, если нужно
            self.scroll_to_element(locator)

            # Ожидаем, что элемент будет доступен для клика
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
            element.click()
            print(f"Клик по элементу с локатором '{locator}'.")
        except Exception as e:
            print(f"Ошибка при клике на элемент с локатором '{locator}': {e}")

    def compare_prices_before_and_after_click(self):
        """
        Функция сравнивает цену до и после клика на кнопку фильтра стоимости.
        1. Получает начальную цену.
        2. Кликает на кнопку для фильтрации стоимости.
        3. Получает обновленную цену.
        4. Сравнивает начальную и обновленную цену.
        """

        # Получаем начальную цену
        initial_price_element = self.get_initial_price()
        initial_price_text = initial_price_element.text.strip()
        print(f"Начальная цена: {initial_price_text}")

        # Кликаем по кнопке фильтра стоимости
        self.click_cost_filter()

        # Ждем обновления элементов с ценой
        WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, self.initial_price_elements))
        )

        # Получаем обновленную цену
        updated_price_element = self.get_filtered_price()
        updated_price_text = updated_price_element.text.strip()
        print(f"Обновленная цена: {updated_price_text}")

        # Сравниваем цены
        if initial_price_text == updated_price_text:
            print("Цены совпадают.")
        else:
            print(
                f"Цены не совпадают! Начальная цена: '{initial_price_text}', обновленная цена: '{updated_price_text}'")

    import re

    def check_prices_increasing(self):
        # Находим все элементы, соответствующие локатору цен
        price_elements = WebDriverWait(self.driver, 180).until(
            EC.presence_of_all_elements_located((By.XPATH, self.initial_price_elements))
        )

        # Извлекаем текст (цену) из каждого элемента и преобразуем в числа
        prices = []
        for price_element in price_elements:
            try:
                # Извлекаем текст и убираем лишние пробелы
                price_text = price_element.text.strip()

                # Убираем слово "от" (и пробелы вокруг) и любые другие ненужные символы (например, валютные символы)
                price_text = price_text.replace("от", "").strip()  # Убираем слово "от"

                # Убираем пробелы между тысячами
                price_text = price_text.replace(" ", "")

                # Убираем возможные пробелы и запятые
                price_text = price_text.replace(",", "").replace("₽", "").strip()

                # Преобразуем текст в число
                price = float(price_text)
                prices.append(price)
            except Exception as e:
                print(f"Ошибка при обработке цены: {e}")
                continue  # Если не получилось извлечь цену, продолжаем с другими элементами

        # Проверяем, что каждая цена больше или равна предыдущей
        for i in range(1, len(prices)):
            assert prices[i] >= prices[
                i - 1], f"Цена на позиции {i} не больше или равна предыдущей: {prices[i]} < {prices[i - 1]}"

        print("Все цены на странице увеличиваются или равны предыдущим.")

    def search_hotel_filter_1(self):
        with allure.step('Применить фильтр Тип размещения'):
            self.get_current_url()  # Печать текущего URL
        # Применяем фильтры
        with allure.step('Проверка работы фильтра'):
            self.check_filtered_hotel_types()

    def search_hotel_filter_2(self):
        with allure.step('Применить фильтр Тип размещения'):
            self.get_current_url()  # Печать текущего URL
        # Применяем фильтры
        with allure.step('Проверка работы фильтра'):
            self.check_filtered_hotel_types()


    # Test case ID 2.14

    def search_hotel_filter_3(self):
        with allure.step('Применить фильтр Звездность 0'):
            self.get_current_url()  # Печать текущего URL
        with allure.step('Проверка работы фильтра'):
            self.check_filtered_hotel_stars()

    def search_hotel_filter_4(self):
        with allure.step('Применить фильтр Звездность 0'):
            self.get_current_url()  # Печать текущего URL
        with allure.step('Проверка работы фильтра'):
            self.check_filtered_hotel_stars()




    # Test case ID 2.9

    def search_hotel_filter_5(self):
        with allure.step('Применить фильтр Стоимость За весь период'):
            self.get_current_url()  # Печать текущего URL
            self.compare_prices_before_and_after_click()

    def search_hotel_filter_6(self):
        with allure.step('Применить фильтр Сначала дешевые'):
            self.get_current_url()  # Печать текущего URL
            self.check_prices_increasing()


    # Test case ID 2.10
    #
    # def search_hotel_filter_1(self):
    #     with allure.step('Применить фильтр Сортировка Сначала Дорогие'):
    #         self.get_current_url()  # Печать текущего URL
    #         self.click_type_hotel_button_1()



