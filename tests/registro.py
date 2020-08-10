import unittest
from selenium import webdriver
import json
from selenium.webdriver.chrome.options import Options
from page_objets.pageindex import PageIndex
from page_objets.pageingresar import PageIngresar
from page_objets.pageregistro import PageRegistro
from page_objets.pageasserts import PageAsserts


class RegistroDonWeb(unittest.TestCase):
    def setUp(self):
        option = Options()
        #option.add_argument('--headless')
        self.driver = webdriver.Chrome('../drivers/chromedriver.exe', options=option)
        self.driver.get('https://donweb.com/es-ar/')
        self.driver.set_window_size(1920, 1080)
        self.IndexPage = PageIndex(self.driver)
        self.IngresarPage = PageIngresar(self.driver)
        self.RegistroPage = PageRegistro(self.driver)
        self.AssertsPage = PageAsserts(self.driver)
        with open("../json/registro.json") as registro:
            self.data_registro = json.loads(registro.read())

    #Intentar registro sin datos
    def test_001_registro(self):
        self.IndexPage.click_boton_inicio()
        self.IngresarPage.click_boton_crear_desde_aqui()
        self.RegistroPage.click_boton_crear_cuenta()
        self.assertEqual(self.AssertsPage.return_block_error(0), 'Campo requerido.')
        self.assertEqual(self.AssertsPage.return_block_error(1), 'Campo requerido.')
        self.assertEqual(self.AssertsPage.return_block_error(2), 'Campo requerido.')
        self.assertEqual(self.AssertsPage.return_block_error(3), 'Campo requerido.')
        self.assertEqual(self.AssertsPage.return_block_error(4), 'El número de teléfono ingresado no es válido.')
        self.assertEqual(self.AssertsPage.return_block_error(5), 'Campo requerido.')

    #Intentar realizar registro de usuario nuevo sin Nombre, Apellido, e Email
    def test_002_registro(self):
        self.IndexPage.click_boton_inicio()
        self.IngresarPage.click_boton_crear_desde_aqui()
        self.RegistroPage.escribir_pais(self.data_registro['datos']['pais'])
        self.RegistroPage.escribir_telefono(self.data_registro['datos']['telefono'])
        self.RegistroPage.escribir_password(self.data_registro['datos']['password'])
        self.RegistroPage.click_boton_crear_cuenta()
        self.assertEqual(self.AssertsPage.return_block_error(0), 'Campo requerido.')
        self.assertEqual(self.AssertsPage.return_block_error(1), 'Campo requerido.')
        self.assertEqual(self.AssertsPage.return_block_error(2), 'Campo requerido.')

    #Intentar realizar registro de usuario nuevo sin País,  Telefono y Contraseña
    def test_003_registro(self):
        self.IndexPage.click_boton_inicio()
        self.IngresarPage.click_boton_crear_desde_aqui()
        self.RegistroPage.escribir_nombre(self.data_registro['datos']['nombre'])
        self.RegistroPage.escribir_apellido(self.data_registro['datos']['apellido'])
        self.RegistroPage.escribir_email(self.data_registro['datos']['email'])
        self.RegistroPage.click_boton_crear_cuenta()
        self.assertEqual(self.AssertsPage.return_block_error(0), 'Campo requerido.')
        self.assertEqual(self.AssertsPage.return_block_error(1), 'El número de teléfono ingresado no es válido.')
        self.assertEqual(self.AssertsPage.return_block_error(2), 'Campo requerido.')

    #Intentar realizar registro de usuario nuevo con nombre y apellido invalidos
    def test_004_registro(self):
        self.IndexPage.click_boton_inicio()
        self.IngresarPage.click_boton_crear_desde_aqui()
        self.RegistroPage.escribir_nombre(self.data_registro['error']['nombre'])
        self.RegistroPage.escribir_apellido(self.data_registro['error']['apellido'])
        self.RegistroPage.escribir_email(self.data_registro['datos']['email'])
        self.RegistroPage.escribir_pais(self.data_registro['catos']['pais'])
        self.RegistroPage.escribir_telefono(self.data_registro['datos']['telefono'])
        self.RegistroPage.escribir_password(self.data_registro['datos']['password'])
        self.RegistroPage.click_boton_crear_cuenta()

    #Intentar realizar registro de usuario nuevo con contraseña corta
    def test_005_registro(self):
        self.IndexPage.click_boton_inicio()
        self.IngresarPage.click_boton_crear_desde_aqui()
        self.RegistroPage.escribir_nombre(self.data_registro['datos']['nombre'])
        self.RegistroPage.escribir_apellido(self.data_registro['datos']['apellido'])
        self.RegistroPage.escribir_email(self.data_registro['datos']['email'])
        self.RegistroPage.escribir_pais(self.data_registro['datos']['pais'])
        self.RegistroPage.escribir_telefono(self.data_registro['datos']['telefono'])
        self.RegistroPage.escribir_password(self.data_registro['error']['password'])
        self.RegistroPage.click_boton_crear_cuenta()
        self.assertEqual(self.AssertsPage.return_block_error(0), 'Debe contener letras y números. Debe contener al'
                                                                 ' menos 8 caracteres.')

    #Intentar realizar registro de usuario con email no valido
    def test_006_registro(self):
        self.IndexPage.click_boton_inicio()
        self.IngresarPage.click_boton_crear_desde_aqui()
        self.RegistroPage.escribir_nombre(self.data_registro['datos']['nombre'])
        self.RegistroPage.escribir_apellido(self.data_registro['datos']['apellido'])
        self.RegistroPage.escribir_email(self.data_registro['error']['email'])
        self.RegistroPage.escribir_pais(self.data_registro['datos']['pais'])
        self.RegistroPage.escribir_telefono(self.data_registro['datos']['telefono'])
        self.RegistroPage.escribir_password(self.data_registro['datos']['password'])
        self.RegistroPage.click_boton_crear_cuenta()
        self.assertEqual(self.AssertsPage.return_block_error(0), 'Email inválido.')

    #Intentar realizar registro de usuario con Contraseña invalida
    def test_007_registro(self):
        self.IndexPage.click_boton_inicio()
        self.IngresarPage.click_boton_crear_desde_aqui()
        self.RegistroPage.escribir_nombre(self.data_registro['datos']['nombre'])
        self.RegistroPage.escribir_apellido(self.data_registro['datos']['apellido'])
        self.RegistroPage.escribir_email(self.data_registro['datos']['email'])
        self.RegistroPage.escribir_pais(self.data_registro['datos']['pais'])
        self.RegistroPage.escribir_telefono(self.data_registro['datos']['telefono'])
        self.RegistroPage.escribir_password(self.data_registro['error2']['password'])
        self.RegistroPage.click_boton_crear_cuenta()
        self.assertEqual(self.AssertsPage.return_block_error(0), 'Debe contener letras y números.')

    #Intentar realizar registro de usuario con una cuenta de Email existente
    def test_008_registro(self):
        self.IndexPage.click_boton_inicio()
        self.IngresarPage.click_boton_crear_desde_aqui()
        self.RegistroPage.escribir_nombre(self.data_registro['datos']['nombre'])
        self.RegistroPage.escribir_apellido(self.data_registro['datos']['apellido'])
        self.RegistroPage.escribir_email(self.data_registro['error2']['email'])
        self.RegistroPage.escribir_pais(self.data_registro['datos']['pais'])
        self.RegistroPage.escribir_telefono(self.data_registro['datos']['telefono'])
        self.RegistroPage.escribir_password(self.data_registro['datos']['password'])
        self.RegistroPage.click_boton_crear_cuenta()
        self.assertEqual(self.AssertsPage.return_block_error(0), 'El email ingresado ya está en uso.')

        #Crear una cuenta exitosamente
    def test_009_registro(self):
        self.IndexPage.click_boton_inicio()
        self.IngresarPage.click_boton_crear_desde_aqui()
        self.RegistroPage.escribir_nombre(self.data_registro['datos']['nombre'])
        self.RegistroPage.escribir_apellido(self.data_registro['datos']['apellido'])
        self.RegistroPage.escribir_email(self.data_registro['datos']['email'])
        self.RegistroPage.escribir_pais(self.data_registro['datos']['pais'])
        self.RegistroPage.escribir_telefono(self.data_registro['datos']['telefono'])
        self.RegistroPage.escribir_password(self.data_registro['datos']['password'])
        self.RegistroPage.click_boton_crear_cuenta()
        self.assertEqual(self.AssertsPage.return_text_ok(), '¡Tu cuenta fue creada con éxito!')
