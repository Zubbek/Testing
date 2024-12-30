from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.credentials import PATH


def chrome_driver():
    path = PATH
    service = Service(path)
    driver_web = webdriver.Chrome(service=service)
    return driver_web
