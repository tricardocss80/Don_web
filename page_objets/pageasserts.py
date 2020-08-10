from selenium.webdriver.common.by import By
from page_objets.pagemetodoscomunes import PageMetodosComunes


class PageAsserts(PageMetodosComunes):
    def __init__(self, driver):
        super().__init__(driver)
        self.bloque_error = (By.XPATH, '//div[@class="invalid-tooltip d-block"]')
        self.text_cuenta_creada = (By.XPATH, '//p[@class="mb-4"]')
        self.driver = driver

    def return_block_error(self, index):
        return self.driver.find_elements(*self.bloque_error)[index].text

    def return_text_ok(self):
        return self.wait_presence(self.text_cuenta_creada).text
