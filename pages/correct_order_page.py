import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from base.base_class import Base
import allure
import unittest
import unittest
class Correct_order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators general
    correct_button = '//button[@data-testid="correct-order-hotel"]'
    check_in_date_calendar = '//div[@data-testid="checkin-date"]'
    check_out_date_calendar = '//div[@data-testid="checkout-date"]'
    nights_count ='//div[@data-testid="nights-count"]//input[@id="nightsCount"]'
    comment_order = '//div[@data-testid="comment"]//input[@id="comment"]'
    last_name_ru = '//input[@id="clients.0.lastNameRu"]'
    last_name_en = '//input[@id="clients.0.lastNameEn"]'
    name_ru = "//input[@id='clients.0.nameRu']"
    name_en = "//input[@id='clients.0.nameEn']"
    father_name_en = "//input[@id='clients.0.middleNameEn']"
    father_name_ru = "//input[@id='clients.0.middleNameRu']"
    total_cost = '//input[@id="totalCost"]'
    payment_method = '//input[@id="paymentMethod"]'
    penalty_date_calendar = '//div[@data-testid="penaltyDate"]//div[@class="react-datepicker__input-container"]'
    phone_number = '//input[@id="clients.0.phone"]'
    phone_hotel_number = '//input[@id="contactInfo"]'
    email = "//input[@id='clients.0.email']"
    save_button = "//button[text()='Сохранить']"
    download_button_1 = '//h2[contains(text(), ".pdf")]'

    # Test ID 2.5
    new_check_in_day_1 = '//div[@class="react-datepicker__day bg-black-05  react-datepicker__day--020"]'
    new_check_out_day_1 = '//div[@class="react-datepicker__day bg-black-05  react-datepicker__day--021"]'

    # Test ID 2.6
    new_check_in_day_2 = '//div[@class="react-datepicker__day bg-black-05  react-datepicker__day--024"]'
    new_check_out_day_2 = '//div[@class="react-datepicker__day bg-black-05  react-datepicker__day--026"]'
    new_penalty_day_1 = '//div[@class="react-datepicker__day bg-black-05  react-datepicker__day--010"]'
    download_button_2 = '//h2[contains(text(), ".pdf")]'

    # Test ID 2.7/2.8/2.9
    download_button_3 = '//h2[contains(text(), ".pdf")]'


    # Assert Vaucher
    comment_check = "//div[contains(@class, 'details')]//h3[text()='Контакты']/following-sibling::p[span[@class='label' and text()='Комментарий']]/span[@class='value']"
    days_check = "//div[contains(@class, 'details')]//h3[text()='Детали размещения']/following-sibling::p[span[@class='label' and text()='Дата заезда / Дата выезда']]/span[@class='value']"
    nights_count_check = "//div[contains(@class, 'details')]//h3[text()='Детали размещения']/following-sibling::p[span[@class='label' and text()='Количество суток']]/span[@class='value']"
    guest_check = "//div[contains(@class, 'details')]//h3[text()='Детали размещения']/following-sibling::p[span[@class='label' and text()='Имя гостя']]/span[@class='value']"
    phone_hotel_check = "//div[contains(@class, 'details')]//h3[text()='Контакты']/following-sibling::p[span[@class='label' and text()='Телефон / Факс / Email']]/span[@class='value']"

    # Getters
    def get_correct_button(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.correct_button)))

    def get_check_in_date_calendar(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.check_in_date_calendar)))

    def get_check_out_date_calendar(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.check_out_date_calendar)))

    def get_nights_count(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.nights_count)))

    def get_comment_order(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.comment_order)))

    def get_last_name_ru(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name_ru)))

    def get_last_name_en(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name_en)))

    def get_name_ru(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.name_ru)))

    def get_name_en(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.name_en)))

    def get_father_name_en(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.father_name_en)))

    def get_father_name_ru(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.father_name_ru)))

    def get_total_cost(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.total_cost)))

    def get_payment_method(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.payment_method)))

    def get_penalty_date_calendar(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.penalty_date_calendar)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_phone_hotel_number(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_hotel_number)))

    def get_email(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_save_button(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.save_button)))

    def get_new_check_in_day_1(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.new_check_in_day_1)))

    def get_new_check_in_day_2(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.new_check_in_day_2)))

    def get_new_check_out_day_1(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.new_check_out_day_1)))

    def get_new_check_out_day_2(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.new_check_out_day_2)))

    def get_new_penalty_day_1(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.new_penalty_day_1)))

    def get_download_button_1(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.download_button_1)))

    def get_download_button_2(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.download_button_2)))

    def get_download_button_3(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.download_button_3)))

    def get_comment_check(self):
        return WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, self.comment_check)))

    def get_days_check(self):
        return WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, self.days_check)))

    def get_nights_count_check(self):
        return WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, self.nights_count_check)))

    def get_guest_check(self):
        return WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, self.guest_check)))

    def get_phone_hotel_check(self):
        return WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, self.phone_hotel_check)))


    # Actions

    # Метод для прокрутки вниз до нужного элемента с плавной анимацией
    def scroll_to_element(self, element):
        # Прокручиваем элемент в видимую область с минимальной прокруткой
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'nearest'});", element)
        print(f"Элемент {element} прокручен в видимую область.")
        WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable(element))
        element.click()
        time.sleep(2)


    def click_correct_button(self):
        with allure.step('Изменить данные'):
            self.get_correct_button().click()
            print('Correct order')

    def scroll_to_top(self):
        # Прокручиваем страницу наверх
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)  # Пауза для ожидания
        print("Страница прокручена вверх.")

    # Test case 2.6
    def click_penalty_date_calendar(self):
        self.scroll_to_top()
        penalty_date_calendar = self.get_penalty_date_calendar()
        self.scroll_to_element(penalty_date_calendar)


    def click_new_penalty_day_1(self):
        with allure.step('Выбрать новую дату штрафа'):
            self.get_new_penalty_day_1().click()
            print('Click new_penalty_day_1')



    def input_payment_method(self, payment):
        with allure.step('Ввести способ новый оплаты'):
            payment_method = self.get_payment_method()
            self.scroll_to_element(payment_method)
            self.get_payment_method().clear()
            self.get_payment_method().send_keys(payment)
            print('Input payment_method')


    def input_nights_count(self, input_nights_count):
        with allure.step('Ввести новое количество ночей'):
            nights_count = self.get_nights_count()
            self.scroll_to_element(nights_count)
            self.get_nights_count().clear()
            self.get_nights_count().send_keys(input_nights_count)
            print('Input nights_count')


    def click_check_in_date_calendar(self):
        self.scroll_to_top()
        check_in_date_calendar = self.get_check_in_date_calendar()
        self.scroll_to_element(check_in_date_calendar)


    def click_new_check_in_day_1(self):
        with allure.step('Выбрать новую дату выезда'):
            self.get_new_check_in_day_1().click()
            print('Click new_check_in_day_1')


    def click_new_check_in_day_2(self):
        with allure.step('Выбрать новую дату выезда'):
            self.get_new_check_in_day_2().click()
            print('Click new_check_in_day_2')

    def click_check_out_date_calendar(self):
        self.get_check_out_date_calendar().click()
        print('Click check_out_date_calendar')


    def click_new_check_out_day_1(self):
        with allure.step('Выбрать новую дату выезда'):
            self.get_new_check_out_day_1().click()
            print('Click new_check_out_day_1')


    def click_new_check_out_day_2(self):
        with allure.step('Выбрать нову дату выезда'):
            self.get_new_check_out_day_2().click()
            print('Click new_check_out_day_1')



    # Test cases all

    def input_comment_order(self, comment):
        with allure.step('Ввести комментарий'):
            comment_order = self.get_comment_order()
            self.scroll_to_element(comment_order)
            self.get_comment_order().clear()
            self.get_comment_order().send_keys(comment)
            print('Input comment_order')


    # Test cases all

    def input_last_name_ru(self, surname):
        with allure.step('Ввести новую фамилию'):
            input_surname = self.get_last_name_ru()
            self.scroll_to_element(input_surname)
            input_surname.clear()
            input_surname.send_keys(surname)
            print('last_name_ru: ' + surname)

    def input_last_name_en(self, surname):
        with allure.step('Ввести новую фамилию'):
            input_surname = self.get_last_name_en()
            self.scroll_to_element(input_surname)
            input_surname.clear()
            input_surname.send_keys(surname)
            print('last_name_en: ' + surname)

    def input_phone_number(self, input_cel_number):
        with allure.step('ввести номер телефона'):
            phone_number = self.get_phone_number()
            self.scroll_to_element(phone_number)
            self.get_phone_number().send_keys(input_cel_number)
            print('input_cel_number')


    def input_phone_hotel_number(self, input_photel_number):
        with allure.step('ввести номер телефона'):
            phone_hotel_number = self.get_phone_hotel_number()
            self.scroll_to_element(phone_hotel_number)
            self.get_phone_hotel_number().send_keys(input_photel_number)
            print('input phone hotel_number')

    def input_email(self, input_email_number):
        with allure.step('ввести email'):
            email_number = self.get_email()
            self.scroll_to_element(email_number)
            self.get_email().send_keys(input_email_number)
            print('input_cel_number')

    def click_save_button(self):
        with allure.step('Нажать "Сохранить"'):
            save_button = self.get_save_button()
            self.scroll_to_element(save_button)
            save_button.click()

    def click_download_button(self):
        with allure.step('Изменить данные'):
            self.scroll_to_top()
            download_button = self.get_correct_button()
            self.scroll_to_element(download_button)
            print('Download order')

    def click_download_vaucher_button_1(self):
        with allure.step('Скачать ваучер'):
            download_vaucher_button_1 = self.get_download_button_1()
            self.scroll_to_element(download_vaucher_button_1)
            print('download_vaucher_button')

    def click_download_vaucher_button_2(self):
        with allure.step('Скачать ваучер'):
            download_vaucher_button_2 = self.get_download_button_2()
            self.scroll_to_element(download_vaucher_button_2)
            print('download_vaucher_button')

    def click_download_vaucher_button_3(self):
        with allure.step('Скачать ваучер'):
            download_vaucher_button_3 = self.get_download_button_3()
            self.scroll_to_element(download_vaucher_button_3)
            print('download_vaucher_button')

    def correct_form_1(self):
        with allure.step('Заполнить и сохранить'):
            self.get_current_url()
            self.click_correct_button()
            self.click_check_in_date_calendar()
            self.click_new_check_in_day_1()
            self.click_check_out_date_calendar()
            self.click_new_check_out_day_1()
            self.input_nights_count(5)
            self.input_comment_order('Заказ на 5 ночей')
            self.input_last_name_ru('Петров')
            self.input_last_name_en('Petrov')
            self.click_save_button()
            self.click_download_button()
            self.click_download_vaucher_button_1()
            self.switch_to_new_window()
            with allure.step('Поле комментарий изменено'):
                comment_element = self.get_comment_check()
                self.assert_word(comment_element, "Заказ на 5 ночей")
            with allure.step('Поле дни заезда/выезда изменено'):
                days_element = self.get_days_check()
                self.scroll_to_element(days_element)
                self.assert_symbol(days_element, "20")
            with allure.step('Количество ночей изменено'):
                nights_count_element = self.get_nights_count_check()
                self.scroll_to_element(nights_count_element)
                self.assert_word(nights_count_element, "5")
            with allure.step('Имя гостя изменено'):
                guest_check_element = self.get_guest_check()
                self.scroll_to_element(guest_check_element)
                # Здесь мы передаем строку 'Иван Петров', и assert_word будет использовать contains для проверки вхождения этой строки
                self.assert_word_1(guest_check_element, "Иван Петров")


    def correct_form_2(self):
        with allure.step('Заполнить и сохранить'):
            self.get_current_url()
            self.click_correct_button()
            self.click_penalty_date_calendar()
            self.click_new_penalty_day_1()
            self.click_check_in_date_calendar()
            self.click_new_check_in_day_2()
            self.click_check_out_date_calendar()
            self.click_new_check_out_day_2()
            self.input_nights_count(3)
            self.input_comment_order('Заказ на 3 ночей')
            self.input_last_name_ru('Петрова')
            self.input_last_name_en('Petrova')
            self.click_save_button()
            self.click_download_button()
            self.click_download_vaucher_button_2()
            self.switch_to_new_window()
            with allure.step('Поле комментарий изменено'):
                comment_element = self.get_comment_check()
                self.assert_word(comment_element, "Заказ на 3 ночей")
            with allure.step('Поле дни заезда/выезда изменено'):
                days_element = self.get_days_check()
                self.scroll_to_element(days_element)
                self.assert_symbol(days_element, "24")
            with allure.step('Количество ночей изменено'):
                nights_count_element = self.get_nights_count_check()
                self.scroll_to_element(nights_count_element)
                self.assert_word(nights_count_element, "3")
            with allure.step('Имя гостя изменено'):
                guest_check_element = self.get_guest_check()
                self.scroll_to_element(guest_check_element)
                self.assert_word_1(guest_check_element, "Петрова")


    def correct_form_3(self):
        with allure.step('Заполнить и сохранить'):
            self.get_current_url()
            self.click_correct_button()
            self.input_phone_number('+756893023948')
            self.click_save_button()
            self.click_download_button()
            self.click_download_vaucher_button_3()
            self.switch_to_new_window()
            with allure.step('Поле комментарий не изменено'):
                comment_element = self.get_comment_check()
                self.assert_word(comment_element, "Комментария нет")
            with allure.step('Имя гостя не изменено'):
                guest_check_element = self.get_guest_check()
                self.scroll_to_element(guest_check_element)
                self.assert_word_1(guest_check_element, "Иванов")

    def correct_form_4(self):
        with allure.step('Заполнить и сохранить'):
            self.get_current_url()
            self.click_correct_button()
            self.input_email('ivan@gmail.com')
            self.click_save_button()
            self.click_download_button()
            self.click_download_vaucher_button_3()
            self.switch_to_new_window()
            with allure.step('Поле комментарий не изменено'):
                comment_element = self.get_comment_check()
                self.assert_word(comment_element, "Комментария нет")
            with allure.step('Имя гостя не изменено'):
                guest_check_element = self.get_guest_check()
                self.scroll_to_element(guest_check_element)
                self.assert_word_1(guest_check_element, "Иванов")

    def correct_form_5(self):
        with allure.step('Заполнить и сохранить'):
            self.get_current_url()
            self.click_correct_button()
            self.input_phone_hotel_number('+756893023948')
            self.click_save_button()
            self.click_download_button()
            self.click_download_vaucher_button_3()
            self.switch_to_new_window()
            with allure.step('Поле комментарий не изменено'):
                comment_element = self.get_comment_check()
                self.assert_word(comment_element, "Комментария нет")
            with allure.step('Имя гостя не изменено'):
                guest_check_element = self.get_guest_check()
                self.scroll_to_element(guest_check_element)
                self.assert_word_1(guest_check_element, "Иванов")
            with allure.step('Поле контакт отеля изменено'):
                phone_hotel_check_element = self.get_phone_hotel_check()
                self.scroll_to_element(phone_hotel_check_element)
                self.assert_word_1(phone_hotel_check_element, "+756893023948")


    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
