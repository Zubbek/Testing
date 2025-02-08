from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.driver_setup import chrome_driver
from utilities.credentials import USERNAME, PASSWORD

def test_sort_products_az():
    driver = chrome_driver()
    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_button.click()

        dropdown = Select(driver.find_element("class name", "product_sort_container"))
        dropdown.select_by_value("az")

        products = driver.find_elements("css selector", ".inventory_item_name")

        product_names = [product.text for product in products]

        assert product_names == sorted(product_names), "Products on the page are not sorted from A-Z"

    except Exception as error:
        print("error occurred: ", error)
        raise

    finally:
        driver.quit()


def test_sort_products_za():
    driver = chrome_driver()
    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_button.click()

        dropdown = Select(driver.find_element("class name", "product_sort_container"))
        dropdown.select_by_value("za")

        products = driver.find_elements("css selector", ".inventory_item_name")

        product_names = [product.text for product in products]

        assert product_names == sorted(product_names, reverse=True), "Products on the page are not sorted from Z-A"

    except Exception as error:
        print("error occurred: ", error)
        raise

    finally:
        driver.quit()

def test_sort_products_pirce_low():
    driver = chrome_driver()
    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_button.click()

        dropdown = Select(driver.find_element("class name", "product_sort_container"))
        dropdown.select_by_value("lohi")

        products = driver.find_elements("css selector", ".inventory_item_price")

        product_price = [float(product.text.replace("$", "")) for product in products]

        print("products: ", product_price)

        assert product_price == sorted(product_price), "Products on the page are not sorted from the lowest Price"

    except Exception as error:
        print("error occurred: ", error)
        raise

    finally:
        driver.quit()

def test_sort_products_pirce_high():
    driver = chrome_driver()
    try:
        driver.get("https://www.saucedemo.com/")

        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_button.click()

        dropdown = Select(driver.find_element("class name", "product_sort_container"))
        dropdown.select_by_value("hilo")

        products = driver.find_elements("css selector", ".inventory_item_price")

        product_price = [float(product.text.replace("$", "")) for product in products]

        print("products: ", product_price)

        assert product_price == sorted(product_price, reverse=True), "Products on the page are not sorted from the highest Price"

    except Exception as error:
        print("error occurred: ", error)
        raise

    finally:
        driver.quit()