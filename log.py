import requests
from requests.models import Response
#import lxml.html as html
from selenium import webdriver   
import time
from time import sleep
from bs4 import BeautifulSoup
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium import webdriver                    # Import module 
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import xlsxwriter
import random

class load(unittest.TestCase):
    def __init__(self):
        self.primer_pagina = "https://www.instagram.com/keukenmeid/?hl=es"
        self._tiempo_primer_pagina = 10

    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get(self.primer_pagina)
        sleep(self._tiempo_primer_pagina)

    def test_instagram(self):
        def login(self):
            driver = self.driver
            login_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Iniciar sesión')
            login_button.click()
            sleep(2)
            try:
                correo = driver.find_element(By.XPATH, "//input[@name = 'username']")
                correo.click()
                correo.send_keys("7443108789")
                print("correo mandado")
                contraseña = driver.find_element(By.XPATH, "//input[@name = 'password']")
                contraseña.send_keys("kroon123#")
                print("contraseña mandada")
                time.sleep(0.5)
                inicio = driver.find_element(By.XPATH, "//button[@class = '_acan _aiit _acap _aijb _acas _aj1-']")
                inicio.click()
                sleep(8)
                print("exito")
            except:
                print('No se pudo entrar')
            noguardar(self)
        def noguardar(self):
            driver = self.driver
            try:
                no = driver.find_element(By.XPATH, "//button[@class = '_acan _aiit _acao _aija _acas _aj1-']")
                no.click()
                print("Paso por ahora no")
                sleep(5)
            except:
                print("No paso por ahora no")
                sleep(1000)
            getlinks(self)
        def getlinks(self):
            driver = self.driver
            try:
                #Incluir button _a9-- _a9_1
                captch = driver.find_element(By.XPATH, "//button[@class = '_a9-- _a9_1']")
                captch.click()
                print("captcha lista")
                sleep(2)
            except:
                print("No captcha")
                pass
            driver.get("https://www.instagram.com/shifrajumelet/?hl=nl")
            sleep(5)
            try:
                links = driver.find_elements(By.XPATH, "//div[@class = '_aabd _aa8k _aanf']/a")
                ligas = [link.get_attribute('href') for link in links]
                print(len(ligas), ligas)
            except:
                print("Error al correr la comprehesion list")
            list_a_excel(self, ligas)
        def list_a_excel(self, ligas):
            driver = self.driver

            #Excel
            archivo = xlsxwriter.Workbook('Text.xlsx')
            hoja = archivo.add_worksheet()
            #Localización
            abajo = 0
            derecha = 0
            hoja.write(abajo, derecha, "Text")
            derecha += 1
            hoja.write(abajo, derecha, "Liga")

            abajo += 1
            derecha = 0

            contador = 1
            for x in ligas:
                driver.get(f"{x}")
                #Destempo
                num_random = random.randint(0, 9)
                new = "3." + str(num_random)
                new = float(new)
                sleep(new)
                hoja.write(abajo,derecha,x)
                derecha += 1
                try:
                    hashtags = driver.find_elements(By.XPATH, "//a[@class = 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd']")
                    lista = [hashtag.get_attribute('innerHTML') for hashtag in hashtags]
                    lista_limpia = ' '.join([str(elem) for elem in lista])
                    hoja.write(abajo,derecha, lista_limpia)
                    #print(lista)
                except:
                    print("Error al extraer hashtags")
                contador = contador + 1
                print(f"Was visited {x}, page {contador} of {len(ligas)} and it took {new} seconds to recover the info")
                abajo += 1
                derecha = 0
            archivo.close()

        login(self)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)