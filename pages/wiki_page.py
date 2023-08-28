from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
import time


class WikiSearch(BaseDriver):
    def __init__(self, driver, wait):
        # super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def history_date_search(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='Automatización - Wikipedia, la enciclopedia libre']")))

    def page_scrollTo(self):
        scroll_amount = 3000
        pageLength = self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(10)