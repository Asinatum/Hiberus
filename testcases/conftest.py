import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    driver_path = r"C:\python\TestFrameworkDemo\chromedriver.exe"
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.google.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()

