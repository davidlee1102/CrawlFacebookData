from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from EVNCrawlFacebook.selenium.config import get_config
import time


def login() -> WebDriver:
    '''Init Webdriver and open facebook login page'''
    cfg = get_config()
    if not cfg:
        return None

    options = webdriver.ChromeOptions()
    prefs = {
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)

    # Specify the path to chromedriver.exe (download and save on your computer)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
    )
    driver.maximize_window()

    # Open the webpage
    driver.get("http://www.facebook.com")

    '''Enter username, password'''
    username: WebElement = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "input[name='email']"
        ))
    )
    password: WebElement = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "input[name='pass']"
        ))
    )

    # Enter username and password
    username.clear()
    username.send_keys(cfg.USERNAME)
    password.clear()
    password.send_keys(cfg.PASSWORD)

    # Target the login button and click it
    WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    ).click()
    time.sleep(10)
    return driver
