import time
import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time

import allure


class Base():
    def __init__(self, driver):
        self.driver = driver


    # method get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        if not get_url:
            print("Ошибка: Текущий URL пустой.")
        print(f"current url: {get_url}")
        return get_url

    # method assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word in result
        print('Good value word')

    def assert_symbol(self, word, result):
        value_word = word.text
        # Разбиваем строку на символы
        value_word_split = value_word.split('.')
        # Проверяем, что хотя бы один символ из результата есть в строке
        assert result in value_word_split, f"Ожидаемое значение '{result}' не найдено в символах строки!"
        print('Good value word')


    def assert_word_1(self, element, text):
        # XPath с использованием contains для поиска элемента с текстом
        xpath = f"//*[contains(text(), '{text}')]"
        # Ищем элементы с данным XPath
        elements = self.driver.find_elements(By.XPATH, xpath)
        # Проверяем, что элемент найден
        assert len(elements) > 0, f"Текст '{text}' не найден в элементах."
        # Проверяем, что элемент отображается
        assert elements[0].is_displayed(), f"Текст '{text}' найден, но элемент скрыт."
        # Если все хорошо, выводим сообщение
        print(f"Текст '{text}' успешно найден и отображается в элементе.")

    def scroll_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def switch_to_new_window(self):
        # Получаем все открытые окна
        windows = self.driver.window_handles
        # Переключаемся на последнее открытое окно (обычно новое окно будет в конце списка)
        self.driver.switch_to.window(windows[-1])

    # Метод для прокрутки страницы наверх
    def scroll_to_top(self):
        # Прокручиваем страницу наверх
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)  # Пауза для ожидания
        print("Страница прокручена вверх.")

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('screen/' + name_screenshot)

    def take_screenshot(self, driver, test_name):
        """
        Метод для захвата скриншота и прикрепления его к отчету Allure.
        """
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_filename = f"screenshots/{test_name}_{timestamp}.png"

        # Создаем директорию, если она не существует
        os.makedirs(os.path.dirname(screenshot_filename), exist_ok=True)

        # Захватываем скриншот
        driver.save_screenshot(screenshot_filename)

        # Прикрепляем скриншот к отчету Allure
        allure.attach.file(screenshot_filename, name=f"Screenshot_{timestamp}",
                           attachment_type=allure.attachment_type.PNG)

    def setUp(self):
        """
        Метод для настройки теста. Здесь можно инициализировать драйвер или выполнить другие действия перед тестом.
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """
        Метод для очистки после теста. Закрывает драйвер.
        """
        if hasattr(self, 'driver'):
            self.driver.quit()

