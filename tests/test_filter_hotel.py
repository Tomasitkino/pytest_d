import time

from selenium import webdriver
import allure
import pytest
from selenium.common import WebDriverException


from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.search_hotel_page import Search_hotel_page
from pages.services_page import Choose_service_page
from pages.filter_hotel_page import Filter_hotel_page

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


@allure.feature('Поиск отеля(филльтр "Тип размещения")')
@allure.story('Test Case ID 2.11(Тип размещения)')
def test_filter_hotel_1(driver):

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

        fhp = Filter_hotel_page(driver)
        fhp.search_hotel_filter_1()
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()

@allure.feature('Поиск отеля(филльтр "Тип размещения")')
@allure.story('Test Case ID 2.12(Тип размещения)')
def test_filter_hotel_2(driver):

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

        fhp = Filter_hotel_page(driver)
        fhp.search_hotel_filter_2()
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()

@allure.feature('Поиск отеля(филльтр "звездность")')
@allure.story('Test Case ID 2.13')
def test_filter_hotel_3(driver):

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

        fhp = Filter_hotel_page(driver)
        fhp.search_hotel_filter_3()
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()


@allure.feature('Поиск отеля(филльтр "звездность")')
@allure.story('Test Case ID 2.14')
def test_filter_hotel_4(driver):

    try:

        login = Login_page(driver)
        login.authorization_manager()

        mp = Main_page(driver)
        mp.choose_clients_1()

        csp = Choose_service_page(driver)
        csp.select_hotels_service()

        shp = Search_hotel_page(driver)
        shp.search_hotel_1()

        time.sleep(3)

        fhp = Filter_hotel_page(driver)
        fhp.search_hotel_filter_4()
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()

@allure.feature('Поиск отеля(фильтр стоимость за период/ночь)')
@allure.story('Test Case ID 2.15')
def test_filter_hotel_5(driver):

    try:

        print('Start Test 1')

        login = Login_page(driver)
        login.authorization_admin()

        mp = Main_page(driver)
        mp.choose_clients_1()

        csp = Choose_service_page(driver)
        csp.select_hotels_service()

        shp = Search_hotel_page(driver)
        shp.search_hotel_1()

        fhp = Filter_hotel_page(driver)
        fhp.search_hotel_filter_5()
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()

@allure.feature('Поиск отеля(фильтры)')
@allure.story('Test Case ID 2.16 (сначала дорогие)')
def test_filter_hotel_6(driver):

    try:

        login = Login_page(driver)
        login.authorization_admin()

        mp = Main_page(driver)
        mp.choose_clients_1()

        csp = Choose_service_page(driver)
        csp.select_hotels_service()

        shp = Search_hotel_page(driver)
        shp.search_hotel_1()

        fhp = Filter_hotel_page(driver)
        fhp.search_hotel_filter_6()
    except Exception as e:
        # В случае ошибки делаем скриншот
        capture_screenshot_on_failure(driver)
        # Пробрасываем исключение дальше, чтобы тест завершился с ошибкой
        raise e
    finally:
        # Закрываем драйвер только после выполнения всех операций, включая скриншот
        driver.quit()



