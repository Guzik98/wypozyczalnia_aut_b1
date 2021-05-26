from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers, login_admin

driver = setup_drivers()
login_admin(driver)
input = [['pracownik@wp.pl', 'pracownik@wp', 'pracownik@wp.pl', 'pracownik@wp.pl'],
         ['Michał', 'Michał', 'Michał', 'Michał'],
         ['Kowalski', 'Kowalski', 'Kowalski', 'Kowalski'],
         ['pracownik', 'pracownik', 'pracownik', 'pracownik'],
         ['+48509993630', '+48509993630', '+4850999363', '+48509993630'],
         ['21052025', '21052025', '21052025', '21052019'],
         ['CAD443124', '54444848', '54444848', '54444848'],
         ['zaq1@WSX', 'zaq1@WSX', 'zaq1@WSX', 'zaq1@WSX'],
         ['zaq1@WSX', 'zaq1@WSX', 'zaq1@WSX', 'zaq1@WSX']
         ]
test = ['T20', 'T21', 'T22', 'T23']
for i in range(4):
    print(f"\nTest  {test[i]}")
    driver.get("http://127.0.0.1:8000/registerEmployee/")
    email_field = driver.find_element_by_name("email")
    fname_field = driver.find_element_by_name("first_name")
    lname_field = driver.find_element_by_name("last_name")
    username_field = driver.find_element_by_name("username")
    phone_number_field = driver.find_element_by_name("phone")
    expire_date_field = driver.find_element_by_name("Data_waznosc_prawo_jazdy")
    document_number_field = driver.find_element_by_name("Nr_dokumentu")
    is_staff_checkbox = driver.find_element_by_name("is_staff")
    is_staff_checkbox.click()
    password1_field = driver.find_element_by_name("password1")
    password2_field = driver.find_element_by_name("password2")
    input_table = [email_field, fname_field, lname_field, username_field, phone_number_field, expire_date_field,
                   document_number_field, password1_field, password2_field]
    submit_button = driver.find_element_by_name("submit")
    for j in range(len(input_table)):
        input_table[j].clear()
        input_table[j].send_keys(input[j][i])
    submit_button.send_keys(Keys.RETURN)
    if driver.current_url == "http://127.0.0.1:8000/":
        print("Test udany")
    else:
        print("Test nieudany")
driver.get("http://127.0.0.1:8000/logout/")
driver.quit()
