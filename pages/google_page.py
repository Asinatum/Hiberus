# import pytest
# from selenium import webdriver
# from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_driver import BaseDriver


class search_google(BaseDriver):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def google_word(self):
        search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='APjFqb']")))
        search_button.send_keys('automatizacion')
        search_button.send_keys(Keys.ENTER)
        time.sleep(2)

    def wiki_search(self):
        search_wiki = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//h3[normalize-space()='Automatización - Wikipedia, la enciclopedia libre']")))
        search_wiki.click()
        time.sleep(2)
