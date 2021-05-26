from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def login_admin(driver):
    driver.get("http://127.0.0.1:8000/login/")
    login, password = "admin@wp.pl", "admin"
    log_field = driver.find_element_by_name("username")
    pass_field = driver.find_element_by_name("password")
    log_confirm = driver.find_element_by_name('submit')
    log_field.send_keys(login)
    pass_field.send_keys(password)
    log_confirm.send_keys(Keys.RETURN)

def setup_drivers():
    PATH = "C:\Program Files\Google\Chrome Beta\Application\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    return driver

def login_user(driver):
    driver.get("http://127.0.0.1:8000/login/")
    login, password = "ktostam@wp.pl", "zaq1@WSX"
    email_field = driver.find_element_by_id("id_username")
    password_field = driver.find_element_by_name("password")
    submit_button = driver.find_element_by_name("submit")
    email_field.send_keys(login)
    password_field.send_keys(password)
    submit_button.send_keys(Keys.RETURN)

def login_user2(driver):
    driver.get("http://127.0.0.1:8000/login/")
    login, password = "ktostam2@wp.pl", "zaq1@WSX"
    email_field = driver.find_element_by_id("id_username")
    password_field = driver.find_element_by_name("password")
    submit_button = driver.find_element_by_name("submit")
    email_field.send_keys(login)
    password_field.send_keys(password)
    submit_button.send_keys(Keys.RETURN)