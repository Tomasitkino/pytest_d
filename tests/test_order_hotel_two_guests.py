import time

from selenium import webdriver
import allure
import pytest
from selenium.common import WebDriverException

from pages.book_page import Book_page
from pages.download_page import Download_page
from pages.fill_form_2_guests_page import Fill_form_page_two_guests
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
# Test case 2.1
@allure.feature('Бронирование отеля(базовые сценарии)')
@allure.story('Test Case 2.25 2 guests')
def test_order_hotel_two_1(driver):

    try:

        print('Start Test 1')

        login = Login_page(driver)
        login.authorization_admin()

        mp = Main_page(driver)
        mp.choose_clients_1()

        csp = Choose_service_page(driver)
        csp.select_hotels_service()

        shp = Search_hotel_page(driver)
        shp.search_hotel_two_guests()

        time.sleep(3)

        fhp = Select_hotel_page(driver)
        fhp.select_random_hotel_action()

        time.sleep(3)

        srp = Select_room_page(driver)
        srp.select_random_room_action()
        time.sleep(3)

        ffp = Fill_form_page(driver)
        ffp.fill_form_two_guests()

        ffp2 = Fill_form_page_two_guests(driver)
        ffp2.fill_form_second()

        bp = Book_page(driver)
        bp.book_hotel()

        time.sleep(2)

        dp = Download_page(driver)
        dp.download_ticket()

        vdp = Vaucher_download_page(driver)
        vdp.vaucher_download_ticket()

        time.sleep(3)
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()


# Test case 2.1
@allure.feature('Бронирование отеля(базовые сценарии)')
@allure.story('Test Case 2.26 2 guests')
def test_order_hotel_two_2(driver):

    try:

        login = Login_page(driver)
        login.authorization_admin()

        mp = Main_page(driver)
        mp.choose_clients_1()

        csp = Choose_service_page(driver)
        csp.select_hotels_service()

        shp = Search_hotel_page(driver)
        shp.search_hotel_two_guests_sochi()

        time.sleep(3)

        fhp = Select_hotel_page(driver)
        fhp.select_random_hotel_action()

        time.sleep(3)

        srp = Select_room_page(driver)
        srp.select_random_room_action()
        time.sleep(3)

        ffp = Fill_form_page(driver)
        ffp.fill_form_two_guests()

        ffp2 = Fill_form_page_two_guests(driver)
        ffp2.fill_form_second()


        bp = Book_page(driver)
        bp.book_hotel()

        time.sleep(2)

        dp = Download_page(driver)
        dp.download_ticket()

        vdp = Vaucher_download_page(driver)
        vdp.vaucher_download_ticket()

        time.sleep(3)
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()


# Test case 2.1
@allure.feature('Бронирование отеля(базовые сценарии)')
@allure.story('Test Case 2.27 2 guests')
def test_order_hotel_two_3(driver):

    try:

        login = Login_page(driver)
        login.authorization_admin()

        mp = Main_page(driver)
        mp.choose_clients_1()

        csp = Choose_service_page(driver)
        csp.select_hotels_service()

        shp = Search_hotel_page(driver)
        shp.search_hotel_two_guests_tver()

        time.sleep(3)

        fhp = Select_hotel_page(driver)
        fhp.select_random_hotel_action()

        time.sleep(3)

        srp = Select_room_page(driver)
        srp.select_random_room_action()
        time.sleep(3)

        ffp = Fill_form_page(driver)
        ffp.fill_form_two_guests()

        ffp2 = Fill_form_page_two_guests(driver)
        ffp2.fill_form_second()


        bp = Book_page(driver)
        bp.book_hotel()

        time.sleep(2)

        dp = Download_page(driver)
        dp.download_ticket()

        vdp = Vaucher_download_page(driver)
        vdp.vaucher_download_ticket()

        time.sleep(3)
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()





