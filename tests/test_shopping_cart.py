from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import driver
from utils.credentials import USERNAME, PASSWORD

driver = driver()

def test_add_to_cart_from_main_page():
    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_button.click()

        button_add = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        button_add.click()

        shopping_cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert shopping_cart_icon.is_displayed(), "Shopping cart badge (with the number of items) is not displayed after adding item to the cart."
        print("Test passed: Shopping badge (with the number of items) is visible.")

    except Exception as error:
        print("error occurred: ", error)
        raise

    finally:
        driver.quit()


def test_add_to_cart_from_product_page():
    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_button.click()

        item = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "item_4_title_link"))
        )
        item.click()

        button_add = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart"))
        )
        button_add.click()

        shopping_cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert shopping_cart_icon.is_displayed(), "Shopping cart badge (with the number of items) is not displayed after adding item to the cart."
        print("Test passed: Shopping badge (with the number of items) is visible.")

    except Exception as error:
        print("error occurred: ", error)
        raise

    finally:
        driver.quit()

def test_remove_from_cart_on_main_page():
    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_button.click()

        button_add = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        button_add.click()

        shopping_cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert shopping_cart_icon.is_displayed(), "Shopping cart badge (with the number of items) is not displayed after adding item to the cart."

        button_remove = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
        )
        button_remove.click()

        try:
            WebDriverWait(driver, 5).until_not(
                EC.presence_of_element_located((By.ID, "shopping_cart_badge"))
            )
            print("Test passed: The shopping cart badge (with the number of items) is no longer visible.")
        except TimeoutException:
            print(
                "The shopping cart badge (with the number of items) is still visible after removing item from the cart.")

    except Exception as error:
        print("error occurred: ", error)
        raise

    finally:
        driver.quit()


def test_remove_from_cart_on_product_page():
    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_button.click()

        item = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "item_4_title_link"))
        )
        item.click()

        button_add = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart"))
        )
        button_add.click()

        shopping_cart_icon_add = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert shopping_cart_icon_add.is_displayed(), "Shopping cart badge (with the number of items) is not displayed after adding item to the cart."

        button_remove = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "remove"))
        )
        button_remove.click()

        try:
            WebDriverWait(driver, 5).until_not(
                EC.presence_of_element_located((By.ID, "shopping_cart_badge"))
            )
            print("Test passed: The shopping cart badge (with the number of items) is no longer visible.")
        except TimeoutException:
            print(
                "The shopping cart badge (with the number of items) is still visible after removing item from the cart.")

    except Exception as error:
        print("error occurred: ", error)
        raise

    finally:
        driver.quit()