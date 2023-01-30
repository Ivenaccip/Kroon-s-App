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

class get_url(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.get("https://www.instagram.com/keukenmeid/?hl=es")
        sleep(10)

    def test_geturl(self):
        driver = self.driver
        current_url = driver.current_url
        print(current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)