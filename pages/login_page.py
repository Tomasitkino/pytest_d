from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure

login_admin = 'super_admin'
pass_admin = 'rXM9NDnVk3X2Pq0'
login_manage = 'manager_vasiliy'
pass_manage = 'yh5KKwpYIvizhGw'
class Login_page(Base):

    url = 'http://api.demlinkatlas.ru/login'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    user_name = '//*[@name="login"]'
    password = '//*[@name="password"]'
    button_login = '//button[text()="Войти"]'
    main_word = "//*[text()='Услуги']"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def input_user_name(self, user_name):
        with allure.step('Ввести логин'):
            self.get_user_name().send_keys(user_name)
            print('Input user name')

    def input_password(self, password):
        with allure.step('Ввести пароль'):
            self.get_password().send_keys(password)
            print('Input password')

    def click_button_login(self):
        with allure.step('Нажать кнопку "Войти"'):
            self.get_button_login().click()
            print('Click button login')


    # Methods
    def authorization_admin(self):
        with allure.step('Авторизация (админ)'):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name(login_admin)
            self.input_password(pass_admin)
            self.click_button_login()
            self.assert_word(self.get_main_word(),'Услуги')

    def authorization_manager(self):
        with allure.step('Авторизация(менеджер)'):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name(login_manage)
            self.input_password(pass_manage)
            self.click_button_login()
            self.assert_word(self.get_main_word(),'Услуги')

