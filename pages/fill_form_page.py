import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from base.base_class import Base
import allure

class Fill_form_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    select_gender_box = '//input[@type="radio" and @value="Мужчина"]'
    input_citizenship = "//input[@id='react-select-2-input']"
    choose_citizenship = '//*[@id="react-select-2-listbox"]//*[@id="react-select-2-option-0"]'
    document_type_button = "//div[@data-testid='clients.0.document-type']"
    choose_document_type = '//*[@id="react-select-3-listbox"]//*[@id="react-select-3-option-0"]'
    input_number_document = "//input[@id='clients.0.documentNumber']"
    status_button = "//div[@data-testid='clients.0.title']"
    choose_status = '//*[@id="react-select-4-listbox"]//*[@id="react-select-4-option-0"]'
    data_issue_calendar = "//div[@data-testid='clients.0.date-begin']"
    data_issue_year = "//*[@data-testid='clients.0.date-begin-year-selector']"
    data_select_year = "//*[@data-testid='clients.0.date-begin-year-dropdown']//li[@data-testid='clients.0.date-begin-year-2110']" # 2015 year
    data_issue_month = "//*[@data-testid='clients.0.date-begin-month-selector']"
    data_select_month = "//div[@class='custom-datepicker-header flex justify-between items-center w-full gap-4 absolute h-20']//div[@class='custom-month-select text-base cursor-pointer']//ul[@class='months-list']//li[@data-testid='clients.0.date-begin-month-10' and text()='ноябрь']" # november
    data_issue_day = '//div[@aria-label="Choose воскресенье, 20 ноября 2005 г."]'
    data_validity_calendar = "//div[@data-testid='clients.0.date-end']"
    data_validity_year = "//div[@class='custom-datepicker-header flex justify-between items-center w-full gap-4 absolute h-20']//div[@class='custom-year-select text-base cursor-pointer']//div[@data-testid='clients.0.date-end-year-selector']//img[@alt='Toggle Year']"
    data_select_year_end = "//div[@class='react-datepicker__header react-datepicker__header--custom']//ul[@class='years-list']//li[@data-testid='clients.0.date-end-year-2141' and text()='2036']"
    data_validity_month = "//div[@data-testid='clients.0.date-end-month-selector']"
    data_select_month_end = "//div[@class='custom-datepicker-header flex justify-between items-center w-full gap-4 absolute h-20']//div[@class='custom-month-select text-base cursor-pointer']//ul[@class='months-list']//li[@data-testid='clients.0.date-end-month-10' and text()='ноябрь']" # november
    data_validity_day = "//div[@aria-label='Choose воскресенье, 30 ноября 2036 г.']" # day 30
    input_surname = "//input[@id='clients.0.lastNameRu']"
    input_name = "//input[@id='clients.0.nameRu']"
    input_father_name = "//input[@id='clients.0.middleNameRu']"
    input_surname_latin = "//input[@id='clients.0.lastNameEn']"
    input_name_latin = "//input[@id='clients.0.nameEn']"
    input_father_name_latin = "//input[@id='clients.0.middleNameEn']"
    birth_calendar = "//div[@data-testid='clients.0.birth-date']"
    birth_year = "//div[@data-testid='clients.0.birth-date-year-selector']"
    select_birth_year = "//div[@class='custom-datepicker-header flex justify-between items-center w-full gap-4 absolute h-20']//div[@class='custom-year-select text-base cursor-pointer']//ul[@class='years-list']//li[@data-testid='clients.0.birth-date-year-2095' and text()='1990']" # 1994 year
    birth_month = "//div[@data-testid='clients.0.birth-date-month-selector']"
    select_birth_month = "//div[@class='custom-datepicker-header flex justify-between items-center w-full gap-4 absolute h-20']//div[@class='custom-month-select text-base cursor-pointer']//ul[@class='months-list']//li[@data-testid='clients.0.birth-date-month-10' and text()='ноябрь']" # november
    birth_day = '//div[@aria-label="Choose четверг, 8 ноября 1990 г."]' # day 8
    input_email = "//input[@id='clients.0.email']"
    input_cel_number = "//input[@id='clients.0.phone']"
    save_button = "//button[text()='Сохранить']"





    # Getters
    def get_select_gender_box(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.select_gender_box)))

    def get_input_citizenship(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.input_citizenship)))

    def get_choose_citizenship(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_citizenship)))

    def get_document_type_button(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.document_type_button)))

    def get_choose_document_type(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_document_type)))

    def get_input_number_document(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.input_number_document)))

    def get_status_button(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.status_button)))

    def get_choose_status(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_status)))

    def get_data_issue_calendar(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_issue_calendar)))

    def get_data_issue_year(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_issue_year)))

    def get_data_select_year(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_select_year)))

    def get_data_issue_month(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_issue_month)))

    def get_data_select_month(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_select_month)))

    def get_data_issue_day(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_issue_day)))

    def get_data_validity_calendar(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_validity_calendar)))

    def get_data_validity_year(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_validity_year)))

    def get_data_select_year_end(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_select_year_end)))

    def get_data_validity_month(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_validity_month)))

    def get_data_select_month_end(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_select_month_end)))

    def get_data_validity_day(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.data_validity_day)))

    def get_input_surname(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.input_surname)))

    def get_input_name(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.input_name)))

    def get_input_father_name(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.input_father_name)))

    def get_input_surname_latin(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.input_surname_latin)))

    def get_input_name_latin(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.input_name_latin)))

    def get_input_father_name_latin(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.input_father_name_latin)))

    def get_birth_calendar(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.birth_calendar)))

    def get_birth_year(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.birth_year)))

    def get_select_birth_year(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.select_birth_year)))

    def get_birth_month(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.birth_month)))

    def get_select_birth_month(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.select_birth_month)))

    def get_birth_day(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.birth_day)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.input_email)))

    def get_input_cel_number(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.input_cel_number)))

    def get_save_button(self):
        return WebDriverWait(self.driver, 180).until(
            EC.element_to_be_clickable((By.XPATH, self.save_button)))


    # Actions

    # Метод для прокрутки вниз до нужного элемента с плавной анимацией
    def scroll_to_element(self, element):
        # Прокручиваем элемент в видимую область с минимальной прокруткой
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'nearest'});", element)
        print(f"Элемент {element} прокручен в видимую область.")
        time.sleep(2)  # Немного ждем, чтобы прокрутка успела завершиться

    def scroll_to_element_bottom(self, element):
        # Прокручиваем страницу до элемента, чтобы он оказался внизу страницы
        self.driver.execute_script("""
            arguments[0].scrollIntoView({behavior: 'smooth', block: 'end'});
        """, element)
        print(f"Элемент {element} прокручен в нижнюю часть страницы.")
        time.sleep(2)  # Немного ждем, чтобы прокрутка успела завершиться

    def scroll_to_element_center(self, element):
        # Прокручиваем элемент в центр видимой области
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        print(f"Элемент {element} прокручен в центр видимой области.")
        time.sleep(2)  # Немного ждем, чтобы прокрутка успела завершиться

    # Метод для прокрутки вниз до элемента с плавным переходом
    def scroll_down(self, element):
        self.scroll_to_element(element)  # Прокручиваем элемент в центр экрана
        time.sleep(2)
        WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable(element))  # Ожидаем кликабельность
        element.click()  # Кликаем по элементу

    # Выбрать пол
    def click_select_gender_box(self):
        with allure.step('Выбрать пол'):
            select_gender_box = self.get_select_gender_box()
            self.scroll_to_element(select_gender_box)
            actions = ActionChains(self.driver)
            actions.move_to_element(select_gender_box).click().perform()
            print('Click gender box')

    # Заполнить поле Гражданство
    def input_country_citizenship(self, input_citizenship):
        with allure.step('Ввести гражданство'):
            self.get_input_citizenship().send_keys(input_citizenship)
            print('Input citizenship')

    def click_choose_citizenship(self):
        self.get_choose_citizenship().click()
        print('Click choose_citizenship')

    # Выбрать тип документа
    def click_document_type_button(self):
        self.get_document_type_button().click()
        print('Click document type button')

    def click_choose_document_type(self):
        with allure.step('Выбрать тип документа'):
            self.get_choose_document_type().click()
            print('Click choose document type')

    # Ввести номер документа
    def input_click_document(self):
        self.get_input_number_document().click()
        print('Input input number document')

    def input_number_doc(self, input_number_document):
        with allure.step('Ввести номер документа'):
            self.get_input_number_document().send_keys(input_number_document)
            print('Input input number document')

    # Выбрать титул

    def click_status_button(self):
        self.get_status_button().click()
        print('Click status button')

    def click_choose_status(self):
        with allure.step('Выбрать титул'):
            self.get_choose_status().click()
            print('Click choose status')

    # Дата выдачи
    def click_data_issue_calendar(self):
        data_issue_calendar = self.get_data_issue_calendar()
        self.scroll_to_element_bottom(data_issue_calendar)  # Прокручиваем к элементу
        data_issue_calendar.click()
        print('Click data issue calendar')

    def click_data_issue_year(self):
        self.get_data_issue_year().click()
        print('Click data issue year')

    def click_data_select_year(self):
        data_select_year = self.get_data_select_year()
        self.scroll_to_element(data_select_year)
        data_select_year.click()

    def click_data_issue_month(self):
        self.get_data_issue_month().click()
        print('Click data issue month')

    def click_data_select_month(self):
        self.get_data_select_month().click()
        print('Click data issue month')

    def click_data_issue_day(self):
        with allure.step('Выбрать дату выдачи документа'):
            self.get_data_issue_day().click()
            print('Click data issue day')

    def click_data_validity_calendar(self):
        self.get_data_validity_calendar().click()
        print('Click data validity calendar')

    def click_data_validity_year(self):
        self.get_data_validity_year().click()
        print('Click validity_year')

    def click_data_select_year_end(self):
        data_select_year_end = self.get_data_select_year_end()
        self.scroll_to_element(data_select_year_end)
        data_select_year_end.click()

    def click_data_validity_month(self):
        self.get_data_validity_month().click()
        print('Click data_validity_month')

    def click_data_select_month_end(self):
        data_select_month_end = self.get_data_select_month_end()
        self.scroll_to_element(data_select_month_end)
        data_select_month_end.click()

    def click_data_validity_day(self):
        with allure.step('Выбрать день окончания действия документа'):
            self.get_data_validity_day().click()
            print('Click data_validity_day')

    def input_ru_surname(self, surname):
        with allure.step('Ввести фамилию на русском'):
            # Получаем элемент ввода для фамилии
            input_surname = self.get_input_surname()
            # Прокручиваем к элементу с центровкой
            self.scroll_to_element_bottom(input_surname)
            # Вводим фамилию в поле
            input_surname.clear()  # Очищаем поле перед вводом, если это необходимо
            input_surname.send_keys(surname)
            print('Фамилия введена: ' + surname)

    def input_ru_name(self, input_name):
        with allure.step('Ввести имя на русском'):
            self.get_input_name().send_keys(input_name)
            print('input_name')

    def input_ru_father_name(self, input_father_name):
        with allure.step('Ввести отчество на русском'):
            self.get_input_father_name().send_keys(input_father_name)
            print('input_father_name')

    def input_en_surname(self, surname):
        with allure.step('Ввести фамилию на английском'):
            input_surname_latin = self.get_input_surname_latin()
            self.scroll_to_element_bottom(input_surname_latin)
            input_surname_latin.clear()  # Очищаем поле перед вводом, если это необходимо
            input_surname_latin.send_keys(surname)

    def input_en_name(self, input_name_latin):
        with allure.step('Ввести имя на английском'):
            self.get_input_name_latin().send_keys(input_name_latin)
            print('input_name')

    def input_en_father_name(self, input_father_name_latin):
        with allure.step('Ввести отчество на английском'):
            self.get_input_father_name_latin().send_keys(input_father_name_latin)
            print('input_father_name')

    def click_birth_calendar(self):
        birth_calendar = self.get_birth_calendar()
        self.scroll_to_element(birth_calendar)
        birth_calendar.click()

    def click_birth_year(self):
        self.get_birth_year().click()
        print('Click birth_year')

    def click_select_birth_year(self):
        select_birth_year = self.get_select_birth_year()
        self.scroll_to_element(select_birth_year)
        select_birth_year.click()

    def click_birth_month(self):
        self.get_birth_month().click()
        print('Click birth_month')

    def click_select_birth_month(self):
        select_birth_month = self.get_select_birth_month()
        self.scroll_to_element(select_birth_month)
        select_birth_month.click()

    def click_birth_day(self):
        with allure.step('Ввести дату рождения'):
            self.get_birth_day().click()
            print('Click birth_day')

    def input_email_form(self, input_email):
        with allure.step('Ввести электронную почту'):
            self.get_input_email().send_keys(input_email)
            print('input_email')

    def input_cell_number(self, input_cel_number):
        with allure.step('ввести номер телефона'):
            self.get_input_cel_number().send_keys(input_cel_number)
            print('input_cel_number')

    def click_save_button(self):
        with allure.step('Нажать "Сохранить"'):
            save_button = self.get_save_button()
            self.scroll_to_element_bottom(save_button)
            save_button.click()

        # Метод для выбора отеля
    def fill_form_1(self):
        with allure.step('Заполнить форму и сохранить'):
            self.get_current_url()  # Печать текущего URL
            self.click_select_gender_box()
            self.input_country_citizenship('Ро')
            self.click_choose_citizenship()
            time.sleep(2)
            self.click_document_type_button()
            self.click_choose_document_type()
            self.input_click_document()
            time.sleep(2)
            self.input_number_doc(2567828390)
            self.click_status_button()
            self.click_choose_status()
            time.sleep(2)
            self.click_data_issue_calendar()
            self.click_data_issue_year()
            self.click_data_select_year()
            self.click_data_issue_month()
            self.click_data_select_month()
            self.click_data_issue_day()
            self.click_data_validity_calendar()
            self.click_data_validity_year()
            self.click_data_select_year_end()
            self.click_data_validity_month()
            self.click_data_select_month_end()
            self.click_data_validity_day()
            self.input_ru_surname('Иванов')
            self.input_ru_name('Иван')
            self.input_ru_father_name('Иванович')
            self.input_en_surname('Ivanov')
            self.input_en_name('Ivan')
            self.input_en_father_name('Ivanovich')
            self.click_birth_calendar()
            self.click_birth_year()
            self.click_select_birth_year()
            self.click_birth_month()
            self.click_select_birth_month()
            self.click_birth_day()
            self.input_email_form('ivanov234@gmail.com')
            self.input_cell_number(9765843562)
            self.click_save_button()

    def fill_form_2(self):
        with allure.step('Заполнить форму и сохранить'):
            self.get_current_url()  # Печать текущего URL
            self.click_select_gender_box()
            self.input_country_citizenship('Ро')
            self.click_choose_citizenship()
            time.sleep(2)
            self.click_document_type_button()
            self.click_choose_document_type()
            self.input_click_document()
            time.sleep(2)
            self.input_number_doc(2567828390)
            self.click_status_button()
            self.click_choose_status()
            time.sleep(2)
            self.click_data_issue_calendar()
            self.click_data_issue_year()
            self.click_data_select_year()
            self.click_data_issue_month()
            self.click_data_select_month()
            self.click_data_issue_day()
            self.click_data_validity_calendar()
            self.click_data_validity_year()
            self.click_data_select_year_end()
            self.click_data_validity_month()
            self.click_data_select_month_end()
            self.click_data_validity_day()
            self.input_ru_surname('Сидр')
            self.input_ru_name('Сидра')
            self.input_ru_father_name('Иванович')
            self.input_en_surname('Ivanov')
            self.input_en_name('Ivan')
            self.input_en_father_name('Ivanovich')
            self.click_birth_calendar()
            self.click_birth_year()
            self.click_select_birth_year()
            self.click_birth_month()
            self.click_select_birth_month()
            self.click_birth_day()
            self.input_email_form('ivanov234@gmail.com')
            self.input_cell_number(9765843562)
            self.click_save_button()


    def fill_form_two_guests(self):
        with allure.step('Заполнить форму и сохранить'):
            self.get_current_url()  # Печать текущего URL
            self.click_select_gender_box()
            self.input_country_citizenship('Ро')
            self.click_choose_citizenship()
            time.sleep(2)
            self.click_document_type_button()
            self.click_choose_document_type()
            self.input_click_document()
            time.sleep(2)
            self.input_number_doc(2567828390)
            self.click_status_button()
            self.click_choose_status()
            time.sleep(2)
            self.click_data_issue_calendar()
            self.click_data_issue_year()
            self.click_data_select_year()
            self.click_data_issue_month()
            self.click_data_select_month()
            self.click_data_issue_day()
            self.click_data_validity_calendar()
            self.click_data_validity_year()
            self.click_data_select_year_end()
            self.click_data_validity_month()
            self.click_data_select_month_end()
            self.click_data_validity_day()
            self.input_ru_surname('Сидр')
            self.input_ru_name('Сидра')
            self.input_ru_father_name('Иванович')
            self.input_en_surname('Ivanov')
            self.input_en_name('Ivan')
            self.input_en_father_name('Ivanovich')
            self.click_birth_calendar()
            self.click_birth_year()
            self.click_select_birth_year()
            self.click_birth_month()
            self.click_select_birth_month()
            self.click_birth_day()
            self.input_email_form('ivanov234@gmail.com')
            self.input_cell_number(9765843562)








