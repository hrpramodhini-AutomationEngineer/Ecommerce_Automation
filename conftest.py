import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture(scope="function")
def setup():
    chrome_options = Options()

    # 🚫 Disable password manager + breach detection
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False  # 👈 IMPORTANT
    }

    chrome_options.add_experimental_option("prefs", prefs)

    # Extra stability options
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver

    time.sleep(5)
    driver.quit()