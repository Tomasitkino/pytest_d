from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure

class Download_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    download_button = '//*[@data-testid="place-order-hotel"]'


    # Getters

    def get_download_button(self):
        return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, self.download_button)))

    # Actions

    def click_download_button(self):
        self.get_download_button().click()
        print('Click download_button')


    # Methods
    def download_ticket(self):
        with allure.step('Выписать'):
            self.get_current_url()
            self.click_download_button()


