from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageMetodosComunes:
    def __init__(self, driver):
        self.driver = driver

    def click_boton(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator)).click()

    def wait_presence(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
