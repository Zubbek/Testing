from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def driver():
    path = "/Users/michalzub/chromedriver-mac-arm64/chromedriver"
    service = Service(path)
    driver_web = webdriver.Chrome(service=service)
    return driver_web
