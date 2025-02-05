import random
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from base.base_class import Base

class Select_hotel_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы для кнопок "Выбрать" (одинаковые для всех отелей)
    select_hotel_buttons = '//button[@data-testid="btn-select-hotel"]'

    aa_hotels = '//div[@class="nights flex items-start w-full flex-col font-normal text-xs leading-[133%] text-black-50 justify-between"]//div[text()="AA"]'

    # Метод для получения всех кнопок "Выбрать"
    def get_all_select_buttons(self):
        return WebDriverWait(self.driver, 180).until(
            EC.presence_of_all_elements_located((By.XPATH, self.select_hotel_buttons))
        )

    # Метод для получения всех элементов с текстом "AA"
    def get_all_aa_elements(self):
        return WebDriverWait(self.driver, 90).until(
            EC.presence_of_all_elements_located((By.XPATH, self.aa_hotels))
        )

    # Метод для выбора случайной кнопки "Выбрать"
    def select_random_hotel(self):
        select_buttons = self.get_all_select_buttons()  # Получаем все кнопки
        if select_buttons:
            # Генерируем случайный индекс для выбора кнопки
            random_button = random.choice(select_buttons)
            print("Выбран случайный отель с кнопкой:", random_button)

            # Прокручиваем кнопку в видимую область, если необходимо
            self.scroll_to_element(random_button)

            # Кликаем по выбранной кнопке
            random_button.click()
            time.sleep(2)  # Немного ждем, чтобы действие завершилось
        else:
            print("Не удалось найти кнопки для выбора отеля.")

    # Метод для выбора случайного отеля с текстом 'AA' и клика по кнопке "Выбрать"
    def select_random_aa_hotel(self):
        aa_elements = self.get_all_aa_elements()  # Получаем все элементы с текстом "AA"
        if aa_elements:
            # Выбираем случайный элемент с текстом "AA"
            random_aa_element = random.choice(aa_elements)
            print("Выбран случайный отель с текстом 'AA':", random_aa_element)

            # Прокручиваем элемент с текстом "AA" в видимую область
            self.scroll_to_element(random_aa_element)

            # Находим кнопку "Выбрать" рядом с этим элементом
            select_button = random_aa_element.find_element(By.XPATH,
                                                            "ancestor::div[contains(@class, 'nights')]/following-sibling::div//button[@data-testid='btn-select-hotel']")

            # Кликаем по кнопке "Выбрать"
            select_button.click()
            time.sleep(2)  # Немного ждем, чтобы действие завершилось
        else:
            print("Не удалось найти элементы с текстом 'AA'.")

    # Метод для прокрутки до элемента
    def scroll_to_element(self, element):
        # Прокручиваем элемент в видимую область с минимальной прокруткой
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'nearest'});", element)
        print(f"Элемент {element} прокручен в видимую область.")
        time.sleep(2)  # Немного ждем, чтобы прокрутка успела завершиться


    # Метод для выбора случайного отеля и логирования действия


    def select_random_hotel_action(self):
        with allure.step('Выбрать случайный отель'):
            self.get_current_url()  # Логируем текущий URL страницы
            self.select_random_hotel()  # Выбираем случайный отель

# Метод для выбора случайного отеля и логирования действия
    def select_random_hotel_action_aa(self):
        with allure.step('Выбрать случайный отель с текстом "AA"'):
            self.get_current_url()  # Логируем текущий URL страницы
            self.select_random_aa_hotel()  # Выбираем случайный отель с текстом "AA"







# import time
#
# import allure
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains
#
# from base.base_class import Base
#
#
# class Select_hotel_page(Base):
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#
#     # Locators
#     # Test case ID 2.1
#     select_hotel_button_1 = '//p[contains(text(), "620149, ул. Академика Бардина, дом 21 а.")]/ancestor::div[@class="wrapper flex justify-start bg-white rounded-3xl h-[160px]"]//button[@data-testid="btn-select-hotel"]'
#
#     # Test case ID 2.2
#     select_hotel_button_2 = '//p[contains(text(), "354024, ул. Горького, д.56")]/ancestor::div[@class="wrapper flex justify-start bg-white rounded-3xl h-[160px]"]//button[@data-testid="btn-select-hotel"]'
#
#     # Test case ID 2.3
#     select_hotel_button_3 = '//p[contains(text(), "109004, улица Николоямская, 38/23, строение 1")]/ancestor::div[@class="wrapper flex justify-start bg-white rounded-3xl h-[160px]"]//button[@data-testid="btn-select-hotel"]'
#
#     # Test case ID 2.4
#     select_hotel_button_4 = '//p[contains(text(), "129366, ул. Ярославская, 15, корпус 3")]/ancestor::div[@class="wrapper flex justify-start bg-white rounded-3xl h-[160px]"]//button[@data-testid="btn-select-hotel"]'
#
#     # Getters
#     def get_select_hotel_button_1(self):
#         return WebDriverWait(self.driver, 180).until(
#             EC.element_to_be_clickable((By.XPATH, self.select_hotel_button_1))
#         )
#
#     def get_select_hotel_button_2(self):
#         return WebDriverWait(self.driver, 180).until(
#             EC.element_to_be_clickable((By.XPATH, self.select_hotel_button_2))
#         )
#
#     def get_select_hotel_button_3(self):
#         return WebDriverWait(self.driver, 180).until(
#             EC.element_to_be_clickable((By.XPATH, self.select_hotel_button_3))
#         )
#
#     def get_select_hotel_button_4(self):
#         return WebDriverWait(self.driver, 180).until(
#             EC.element_to_be_clickable((By.XPATH, self.select_hotel_button_4)))
#
#     # Actions
#
#     # Метод для скролла вправо до конца страницы
#     def scroll_right_to_end(self):
#         # Прокручиваем вправо до конца с ограничением
#         current_scroll_position = self.driver.execute_script("return window.scrollX;")  # Текущая позиция прокрутки
#         self.driver.execute_script(f"window.scrollTo({current_scroll_position + 1000}, 0);")  # Прокручиваем на 1000px вправо
#         time.sleep(1)
#
#         # Проверка, если мы достигли края
#         new_scroll_position = self.driver.execute_script("return window.scrollX;")
#         if new_scroll_position == current_scroll_position:
#             print("Достигнут край страницы.")
#         else:
#             print(f"Прокрутили на {new_scroll_position - current_scroll_position}px вправо.")
#         time.sleep(1)
#
#     # Метод для прокрутки вниз до нужного элемента с плавной анимацией
#     def scroll_to_element(self, element):
#         # Прокручиваем элемент в видимую область с минимальной прокруткой
#         self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'nearest'});", element)
#         print(f"Элемент {element} прокручен в видимую область.")
#         time.sleep(2)  # Немного ждем, чтобы прокрутка успела завершиться
#
#     # Метод для прокрутки вправо и затем вниз до элемента с плавным переходом
#     def scroll_right_and_down(self, element):
#         self.scroll_right_to_end()
#         time.sleep(1)  # Немного ждем, чтобы прокрутка завершилась
#         self.scroll_to_element(element)  # Прокручиваем элемент в центр экрана
#         time.sleep(2)
#         WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable(element))  # Ожидаем кликабельность
#         element.click()  # Кликаем по элементу
#
#     # Метод для клика по кнопке "Выбрать" Test case ID 2.1
#     def click_select_button_1(self):
#         select_button_1 = self.get_select_hotel_button_1()
#         self.scroll_right_and_down(select_button_1)  # Прокручиваем вправо и вниз, затем кликаем
#
#     # Test case ID 2.2
#     def click_select_button_2(self):
#         select_button_2 = self.get_select_hotel_button_2()
#         self.scroll_right_and_down(select_button_2)
#
#     # Test case ID 2.3
#     def click_select_button_3(self):
#         select_button_3 = self.get_select_hotel_button_3()
#         self.scroll_right_and_down(select_button_3)
#
#     # Test case ID 2.4
#     def click_select_button_4(self):
#         select_button_4 = self.get_select_hotel_button_4()
#         self.scroll_right_and_down(select_button_4)
#
#
#     # Метод для выбора отеля
#     # Test case ID 2.1
#     def select_hotel_1(self):
#         with allure.step('Выбрать отель'):
#             self.get_current_url()  # Печать текущего URL
#             self.click_select_button_1()
#
#     # Test case ID 2.2
#     def select_hotel_2(self):
#         with allure.step('Выбрать отель'):
#             self.get_current_url()  # Печать текущего URL
#             self.click_select_button_2()
#
#
#     # Test case ID 2.3
#     def select_hotel_3(self):
#         with allure.step('Выбрать отель'):
#             self.get_current_url()  # Печать текущего URL
#             self.click_select_button_3()
#
#     # Test case ID 2.4
#     def select_hotel_4(self):
#         with allure.step('Выбрать отель'):
#             self.get_current_url()  # Печать текущего URL
#             self.click_select_button_4()
