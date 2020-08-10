from page_objets.pagemetodoscomunes import PageMetodosComunes
from selenium.webdriver.common.by import By


class PageRegistro(PageMetodosComunes):
    def __init__(self, driver):
        super().__init__(driver)
        self.intput_nombre = (By.ID, 'name')
        self.intput_apellido = (By.ID, 'lastname')
        self.intput_email = (By.ID, 'email')
        self.dropdown_pais = (By.XPATH, '//div[@class="ng-input"]//input')
        self.dropdown_pais_select = (By.XPATH, '//span[@class="ng-option-label"]')
        self.intput_cod_pais = (By.ID, 'countryCode')
        self.intput_telefono = (By.ID, 'number')
        self.intput_pass = (By.ID, 'password')
        self.button_crear_cuenta = (By.XPATH, '//button[@class="btn btn-success btn-block"]')
        self.driver = driver

    def escribir_nombre(self, data_registro):
        self.wait_presence(self.intput_nombre).send_keys(data_registro)

    def escribir_apellido(self, data_registro):
        self.wait_presence(self.intput_apellido).send_keys(data_registro)

    def escribir_email(self, data_registro):
        self.wait_presence(self.intput_email).send_keys(data_registro)

    def escribir_pais(self, data_registro):
        self.wait_presence(self.dropdown_pais).send_keys(data_registro)
        self.wait_presence(self.dropdown_pais_select).click()

    def escribir_cod_pais(self, data_registro):
        self.wait_presence(self.intput_cod_pais).send_keys(data_registro)

    def escribir_telefono(self, data_registro):
        self.wait_presence(self.intput_telefono).send_keys(data_registro)

    def escribir_password(self, data_registro):
        self.wait_presence(self.intput_pass).send_keys(data_registro)

    def click_boton_crear_cuenta(self):
        self.click_boton(self.button_crear_cuenta)
