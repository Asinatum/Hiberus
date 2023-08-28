import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver_path = r"C:\python\TestFrameworkDemo\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)
driver.get("https://es.wikipedia.org/wiki/Automatizaci%C3%B3n")
driver.maximize_window()
time.sleep(5)

# Ajustar el valor de desplazamiento
scroll_amount = 3000  # Ajusta este valor según la cantidad de desplazamiento deseada

# Realizar un solo scroll
driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
time.sleep(10)  # Espera para permitir que la página se cargue

# Cerrar el navegador
driver.quit()