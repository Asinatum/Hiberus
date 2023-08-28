# import time
import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
from pages.google_page import search_google
from pages.wiki_page import WikiSearch



@pytest.mark.usefixtures("setup")
class TestGoogleSearch():
    def test_google_word(self):
        self.driver.implicitly_wait(30)
        sg = search_google(self.driver, self.wait)
        sw = WikiSearch(self.driver, self.wait)
        sg.google_word()
        sg.wiki_search()
        sw.page_scrollTo()
        sw.screenshot()





