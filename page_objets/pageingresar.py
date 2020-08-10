from selenium.webdriver.common.by import By
from page_objets.pagemetodoscomunes import PageMetodosComunes


class PageIngresar(PageMetodosComunes):
    def __init__(self, driver):
        super().__init__(driver)
        self.button_crear_cuenta = (By.XPATH, '//a[contains(text(),"Créala desde aquí.")]')

        self.driver = driver

    def click_boton_crear_desde_aqui(self):
        self.click_boton(self.button_crear_cuenta)
