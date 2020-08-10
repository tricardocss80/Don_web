from selenium.webdriver.common.by import By
from page_objets.pagemetodoscomunes import PageMetodosComunes


class PageIndex(PageMetodosComunes):
    def __init__(self, driver):
        super().__init__(driver)
        self.button_ingresar = By.XPATH, '//div[@class="btn secundario"]'
        self.driver = driver

    def click_boton_inicio(self):
        self.click_boton(self.button_ingresar)


