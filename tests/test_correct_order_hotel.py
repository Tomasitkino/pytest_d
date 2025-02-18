import time
import pytest

from selenium import webdriver
from selenium.common import WebDriverException

import allure

from pages.book_page import Book_page
from pages.correct_order_page import Correct_order_page
from pages.download_page import Download_page
from pages.fill_form_page import Fill_form_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.search_hotel_page import Search_hotel_page
from pages.select_hotel_page import Select_hotel_page
from pages.select_room_page import Select_room_page
from pages.services_page import Choose_service_page
from pages.vaucher_download_page import Vaucher_download_page

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def capture_screenshot_on_failure(driver):
    """Функция для захвата скриншота в случае ошибки в тесте и прикрепления его в Allure отчет"""
    try:
        timestamp = int(time.time())
        screenshot_path = f"screenshot_failure_{timestamp}.png"

        # Проверяем, активна ли сессия WebDriver перед захватом скриншота
        if driver:
            driver.save_screenshot(screenshot_path)
            print(f"Скриншот сохранен при ошибке по пути: {screenshot_path}")

            # Прикрепляем скриншот в Allure отчет
            with open(screenshot_path, 'rb') as f:
                allure.attach(f.read(), name=f"Failure screenshot {timestamp}", attachment_type=allure.attachment_type.PNG)
        else:
            print("Ошибка: драйвер уже не активен, скриншот не был сделан.")

    except WebDriverException as e:
        print(f"Ошибка при попытке сделать скриншот: {e}")
# Test case 2.6
@allure.feature('Корректировка бронирования')
@allure.story('Test Case ID 2.6')
def test_correct_order_hotel_1(driver):

    try:

        login = Login_page(driver)
        login.authorization_admin()

        mp = Main_page(driver)
        mp.choose_clients_1()

        csp = Choose_service_page(driver)
        csp.select_hotels_service()

        shp = Search_hotel_page(driver)
        shp.search_hotel_1()

        time.sleep(3)

        fhp = Select_hotel_page(driver)
        fhp.select_random_hotel_action()

        time.sleep(3)

        srp = Select_room_page(driver)
        srp.select_random_room_action()
        time.sleep(3)


        ffp = Fill_form_page(driver)
        ffp.fill_form_1()

        bp = Book_page(driver)
        bp.book_hotel()

        dp = Download_page(driver)
        dp.download_ticket()

        cp = Correct_order_page(driver)
        cp.correct_form_1()

        time.sleep(3)
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        pass


@allure.feature('Корректировка бронирования')
@allure.story('Test Case ID 2.7')
def test_correct_order_hotel_2(driver):

    try:

        login = Login_page(driver)
        login.authorization_admin()

        mp = Main_page(driver)
        mp.choose_clients_1()

        csp = Choose_service_page(driver)
        csp.select_hotels_service()

        shp = Search_hotel_page(driver)
        shp.search_hotel_2()

        time.sleep(3)

        fhp = Select_hotel_page(driver)
        fhp.select_random_hotel_action()

        time.sleep(3)

        srp = Select_room_page(driver)
        srp.select_random_room_action()
        time.sleep(3)

        ffp = Fill_form_page(driver)
        ffp.fill_form_2()

        bp = Book_page(driver)
        bp.book_hotel()

        dp = Download_page(driver)
        dp.download_ticket()

        cp = Correct_order_page(driver)
        cp.correct_form_2()

        time.sleep(3)
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()


@allure.feature('Корректировка бронирования')
@allure.story('Test Case ID 2.8')
def test_correct_order_hotel_3(driver):

    try:

        login = Login_page(driver)
        login.authorization_admin()

        mp = Main_page(driver)
        mp.choose_clients_1()

        csp = Choose_service_page(driver)
        csp.select_hotels_service()

        shp = Search_hotel_page(driver)
        shp.search_hotel_1()

        time.sleep(3)

        fhp = Select_hotel_page(driver)
        fhp.select_random_hotel_action()

        time.sleep(3)

        srp = Select_room_page(driver)
        srp.select_random_room_action()
        time.sleep(3)

        ffp = Fill_form_page(driver)
        ffp.fill_form_1()

        bp = Book_page(driver)
        bp.book_hotel()

        dp = Download_page(driver)
        dp.download_ticket()

        cp = Correct_order_page(driver)
        cp.correct_form_3()

        time.sleep(3)
    except Exception as e:
    # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()


@allure.feature('Корректировка бронирования')
@allure.story('Test Case ID 2.9')
def test_correct_order_hotel_4(driver):

    try:

        login = Login_page(driver)
        login.authorization_admin()

        mp = Main_page(driver)
        mp.choose_clients_1()

        csp = Choose_service_page(driver)
        csp.select_hotels_service()

        shp = Search_hotel_page(driver)
        shp.search_hotel_1()

        time.sleep(3)

        fhp = Select_hotel_page(driver)
        fhp.select_random_hotel_action()

        time.sleep(3)

        srp = Select_room_page(driver)
        srp.select_random_room_action()
        time.sleep(3)

        ffp = Fill_form_page(driver)
        ffp.fill_form_1()

        bp = Book_page(driver)
        bp.book_hotel()

        dp = Download_page(driver)
        dp.download_ticket()

        cp = Correct_order_page(driver)
        cp.correct_form_4()

        time.sleep(3)
    except Exception as e:
    #В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()


@allure.feature('Корректировка бронирования')
@allure.story('Test Case ID 2.10')
def test_correct_order_hotel_5(driver):

    try:

        login = Login_page(driver)
        login.authorization_admin()

        mp = Main_page(driver)
        mp.choose_clients_1()

        csp = Choose_service_page(driver)
        csp.select_hotels_service()

        shp = Search_hotel_page(driver)
        shp.search_hotel_1()

        time.sleep(3)

        fhp = Select_hotel_page(driver)
        fhp.select_random_hotel_action()

        time.sleep(3)

        srp = Select_room_page(driver)
        srp.select_random_room_action()
        time.sleep(3)

        ffp = Fill_form_page(driver)
        ffp.fill_form_1()

        bp = Book_page(driver)
        bp.book_hotel()

        dp = Download_page(driver)
        dp.download_ticket()

        cp = Correct_order_page(driver)
        cp.correct_form_5()

        time.sleep(3)
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()



#
#
