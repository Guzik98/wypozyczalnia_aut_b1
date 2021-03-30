from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def login(driver):
    driver.get("http://127.0.0.1:8000/login/")
    login, password = "admin@wp.pl", "admin"
    log_field = driver.find_element_by_name("username")
    pass_field = driver.find_element_by_name("password")
    log_confirm =  driver.find_element_by_name('loguj')
    log_field.send_keys(login)
    pass_field.send_keys(password)
    log_confirm.send_keys(Keys.RETURN)

def setup_drivers():
    PATH = "C:\Program Files\Google\Chrome Beta\Application\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    return driver
