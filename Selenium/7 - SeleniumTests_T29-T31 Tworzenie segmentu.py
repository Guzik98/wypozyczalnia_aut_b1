from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers, login_admin
from os.path import abspath

driver = setup_drivers()
login_admin(driver)
input_table = ['E', '', 'E']
tests = ["T29", "T30", "T31"]
for i in range(3):
    print(f"\nTest: {tests[i]}")
    driver.get("http://127.0.0.1:8000/addSegment/")
    name_field = driver.find_element_by_name("name")
    submit_button = driver.find_element_by_name("submit")
    name_field.send_keys(input_table[i])
    submit_button.click()
    if driver.current_url == "http://127.0.0.1:8000/":
        print("Test udany")
    else:
        print("Test nieudany")
driver.get("http://127.0.0.1:8000/logout/")
driver.quit()