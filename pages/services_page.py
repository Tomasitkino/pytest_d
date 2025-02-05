from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure

class Choose_service_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # locators

    hotels_service = "//button[.//img[@alt='hotel'] and contains(text(), 'Гостиницы')]"

    # Getters

    def get_hotels_service(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.hotels_service)))

    # Actions

    def click_hotels_service(self):
        self.get_hotels_service().click()
        print('Click button hotels service')


    # Methods
    def select_hotels_service(self):
        with allure.step('Выбрать категорию услуг "Гостиницы"'):
            self.get_current_url()
            self.click_hotels_service()


