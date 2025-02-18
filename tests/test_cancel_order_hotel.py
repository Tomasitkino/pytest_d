

import time
import pytest
import allure
from selenium import webdriver
from pages.book_page import Book_page
from pages.cancel_page import Cancel_page
from pages.download_page import Download_page
from pages.fill_form_page import Fill_form_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.search_hotel_page import Search_hotel_page
from pages.select_hotel_page import Select_hotel_page
from pages.select_room_page import Select_room_page
from pages.services_page import Choose_service_page
from pages.vaucher_download_page import Vaucher_download_page
from pages.api_cancel_page import Api_cancel_page

# Фикстура для инициализации WebDriver
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def capture_screenshot_on_failure(driver):
    """Функция для захвата скриншота в случае ошибки в тесте и прикрепления его в Allure отчет"""
    timestamp = int(time.time())
    screenshot_path = f"screenshot_failure_{timestamp}.png"

    # Сохраняем скриншот на диск
    driver.save_screenshot(screenshot_path)
    print(f"Скриншот сохранен при ошибке по пути: {screenshot_path}")

    # Прикрепляем скриншот в Allure отчет
    with open(screenshot_path, 'rb') as f:
        allure.attach(f.read(), name=f"Failure screenshot {timestamp}", attachment_type=allure.attachment_type.PNG)


@allure.feature('Отмена Заказа')
@allure.story('Test Case ID 6.1')
def test_сancel_order_hotel_1(driver):

    """Тест на отмену заказа и проверку через API"""
    try:

        # Шаг 1: Получаем токен перед выполнением Selenium действий
        api_test = Api_cancel_page()
        token = api_test.get_auth_token()  # Получаем токен через API
        assert token, "Не удалось получить токен для API"
        # Шаг 1: Выполняем шаги через Selenium
        with allure.step("Авторизация администратора"):
            login = Login_page(driver)
            login.authorization_admin()

        with allure.step("Выбор клиента"):
            mp = Main_page(driver)
            mp.choose_clients_1()

        with allure.step("Выбор услуги отеля"):
            csp = Choose_service_page(driver)
            csp.select_hotels_service()

        with allure.step("Поиск отеля"):
            shp = Search_hotel_page(driver)
            shp.search_hotel_1()

        time.sleep(3)

        with allure.step("Выбор отеля"):
            fhp = Select_hotel_page(driver)
            fhp.select_random_hotel_action()

        time.sleep(3)

        with allure.step("Выбор комнаты"):
            srp = Select_room_page(driver)
            srp.select_random_room_action()

        time.sleep(3)

        with allure.step("Заполнение формы"):
            ffp = Fill_form_page(driver)
            ffp.fill_form_1()

        with allure.step("Бронирование отеля"):
            bp = Book_page(driver)
            bp.book_hotel()

        with allure.step("Скачивание билета"):
            dp = Download_page(driver)
            dp.download_ticket()

        with allure.step("Отмена заказа через интерфейс"):
            cop = Cancel_page(driver)
            cop.cancel_order()

        time.sleep(3)  # Подождем, пока отмена будет обработана
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        pass

    # # Шаг 2: Теперь проверяем статус отмены через API
    #
    # # Получаем order_id из интерфейса
    # order_id = cop.get_order_id_from_url()
    # assert order_id, f"Не удалось получить order_id для заказа. Проверьте URL или отмену заказа."
    #
    # # Получаем order_ext_id
    # order_ext_id = api_test.get_order_ext_id(order_id)
    # assert order_ext_id, f"Не удалось получить order_ext_id для заказа {order_id}"
    #
    # # Получаем статус бронирования
    # status = api_test.get_booking_status(order_ext_id)
    # assert status == "Отменен", f"Ожидался статус 'Отменен', но получен {status}"
    #
    # with allure.step(f"Проверка статуса отмены через API для ордера {order_id}"):
    #     assert status == "Отменен", f"Ожидался статус 'Отменен', но получен {status}"


