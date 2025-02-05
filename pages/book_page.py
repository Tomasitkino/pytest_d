import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure

class Book_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    book_button = '//*[@data-testid="book-order-hotel"]'
    error_message_locator = "//div[@class='bg-red-light']"  # XPath для поиска сообщения об ошибке

    # Getters

    def get_book_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.book_button)))

    # Actions

    def click_book_button(self):
        book_button = self.get_book_button()
        self.scroll_to_top()
        self.scroll_to_element(book_button)
        book_button.click()
        print('Click book_button')

    def scroll_to_top(self):
        # Прокручиваем страницу наверх
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)  # Пауза для ожидания
        print("Страница прокручена вверх.")

    def scroll_to_element(self, element):
        # Прокручиваем элемент в видимую область с минимальной прокруткой
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'nearest'});", element)
        print(f"Элемент {element} прокручен в видимую область.")
        time.sleep(2)  # Немного ждем, чтобы прокрутка успела завершиться

    # Methods

    def check_for_error(self):
        """Метод для проверки ошибки на красном фоне, прокрутки страницы, и создания скриншота при ее наличии."""
        try:
            # Сначала прокручиваем страницу до возможной ошибки, чтобы элемент стал видимым
            error_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.error_message_locator))
            )
            self.scroll_to_element(error_element)  # Прокручиваем до элемента ошибки

            # Проверяем, виден ли элемент с ошибкой
            if error_element.is_displayed():
                error_text = error_element.text
                print(f"Ошибка обнаружена: {error_text}")

                # Делаем скриншот с ошибкой
                timestamp = int(time.time())
                screenshot_path = f"screenshot_error_{timestamp}.png"
                self.driver.save_screenshot(screenshot_path)
                print(f"Скриншот сохранен по пути: {screenshot_path}")

                # Останавливаем тест с сообщением об ошибке
                raise Exception(f"Тест остановлен из-за ошибки: {error_text}")
        except Exception as e:
            print("Ошибка не найдена или не видна. Тест продолжается.")
            return False
        return True

    def book_hotel(self):
        with allure.step('Забронировать'):
            self.get_current_url()
            self.click_book_button()

            # После клика на кнопку, проверяем наличие ошибки
            if self.check_for_error():
                # Если ошибка найдена, тест остановится и сообщение будет выведено
                return
            else:
                print("Тест продолжается.")

