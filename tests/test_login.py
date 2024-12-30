from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import driver
from utils.credentials import *

driver = driver()


def test_valid_login():
    try:
        driver.get("https://www.saucedemo.com/")
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_button.click()

        title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )

        assert "Products" in title.text, "Title is not displayed"
        print("Login successfully ended!")

    except Exception as error:
        print(error)

    finally:
        driver.quit()


def test_invalid_username_login():
    try:
        driver.get("https://www.saucedemo.com/")
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys(WRONG_USERNAME)
        password.send_keys(PASSWORD)
        login_button.click()

        error_container = driver.find_element(By.CLASS_NAME, "error-message-container")
        if error_container.is_displayed():
            print("Successfully displayed error message!")

    except Exception as error:
        print(error)

    finally:
        driver.quit()


def test_invalid_password_login():
    try:
        driver.get("https://www.saucedemo.com/")
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys(USERNAME)
        password.send_keys(WRONG_PASSWORD)
        login_button.click()

        error_container = driver.find_element(By.CLASS_NAME, "error-message-container")
        if error_container.is_displayed():
            print("Successfully displayed error message!")

    except Exception as error:
        print(error)

    finally:
        driver.quit()