import time

from selenium import webdriver
import allure

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


# #
# # Бронирование АА
# @allure.feature('Бронирование отеля(базовые сценарии)')
# @allure.story('Test Case ID 2.4 (Москва 26.03/28.03)')
# def test_order_hotel_aa():
#     # options = webdriver.ChromeOptions()
#     # options.add_argument('--headless')  # Это включает режим headless
#     # options.add_argument('--disable-gpu')  # Отключаем GPU, для возможных проблем на некоторых системах
#     #
#     # driver = webdriver.Chrome(options=options)  # Передаем опции при создании драйвера
#     driver = webdriver.Chrome()
#
#
#     print('Start Test AA')
#
#     login = Login_page(driver)
#     login.authorization_admin()
#
#     mp = Main_page(driver)
#     mp.choose_clients_prod()
#
#     csp = Choose_service_page(driver)
#     csp.select_hotels_service()
#
#     shp = Search_hotel_page(driver)
#     shp.search_hotel_AA()
#
#     time.sleep(3)
#
#
#     fhp = Select_hotel_page(driver)
#     fhp.select_random_hotel_action_aa()
#
#     time.sleep(3)
#     #
#     srp = Select_room_page(driver)
#     srp.select_random_room_action_aa()
#     time.sleep(3)
#
#     ffp = Fill_form_page(driver)
#     ffp.fill_form_2()
#
#     bp = Book_page(driver)
#     bp.book_hotel()
#
#     dp = Download_page(driver)
#     dp.download_ticket()
#
#     vdp = Vaucher_download_page(driver)
#     vdp.vaucher_download_ticket()
#
#     time.sleep(3)
#
#     cop = Cancel_page(driver)
#     cop.cancel_order()



