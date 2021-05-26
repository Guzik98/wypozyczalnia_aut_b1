from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers

driver = setup_drivers()
input = [['ktam@wp.pl', 'ktostam@wp.pl', 'ktostam@wp.pl'], ['zaq1@WSX', 'zaq1@WSK', 'zaq1@WSX']]
test = ['T7', 'T8', 'T6', 'T9']
for i in range(3):
    print(f"\nTest  {test[i]}")
    driver.get("http://127.0.0.1:8000/login/")
    email_field = driver.find_element_by_id("id_username")
    password_field = driver.find_element_by_name("password")
    submit_button = driver.find_element_by_name("submit")
    email_field.send_keys(input[0][i])
    password_field.send_keys(input[1][i])
    submit_button.send_keys(Keys.RETURN)
    if driver.current_url == "http://127.0.0.1:8000/":
        print("Test udany")
    else:
        print("Test nieudany")
print("\nTest T9")
driver.get("http://127.0.0.1:8000/logout/")
print("Test udany")
driver.quit()