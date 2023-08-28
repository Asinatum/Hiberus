import time
from PIL import Image
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);return document.body.scrollHeight;")
        match = False
        while not match:
            lastCount = pageLength
            time.sleep(3)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);return document.body.scrollHeight;")
            if lastCount == pageLength:
                match = True

    def screenshot(self):
        self.driver.save_screenshot("Wiki_Primer_automation.png")




