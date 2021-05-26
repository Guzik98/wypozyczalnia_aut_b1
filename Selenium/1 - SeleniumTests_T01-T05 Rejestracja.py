from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers

driver = setup_drivers()
input = [["ktostam@wp.pl", "ktośtam@wp.pl", "ktostam@wp.pl", "ktostam@wp.pl", "ktostam@wp.pl"],
['jauzytkownik', "jauzytkownik", "jauzytkownik", "jauzytkownik", "jauzytkownik"],
['Michał', 'Michał', 'Michał', 'Michał', 'Michał'],
['Kowalski', 'Kowalski', 'Kowalski', 'Kowalski', 'Kowalski'],
['+48509993630', '+48509993630', '9993630', '+48509993630', '+48509993630'],
['21052025', '21052025', '21052025', '21052020', '21052025'],
['544448481', '544448481', '544448481', '544448481', '5444484833423424'],
['zaq1@WSX', 'zaq1@WSX', 'zaq1@WSX', 'zaq1@WSX', 'zaq1@WSX'],
['zaq1@WSX', 'zaq1@WSX', 'zaq1@WSX', 'zaq1@WSX', 'zaq1@WSX']]
test = ['T1', 'T2', 'T3', 'T4', 'T5']
for i in range(5):
    print(f"\nTest  {test[i]}")
    driver.get("http://127.0.0.1:8000/register/")
    email_field = driver.find_element_by_name("email")
    username_field = driver.find_element_by_name("username")
    first_name_field = driver.find_element_by_name("first_name")
    last_name_field = driver.find_element_by_name("last_name")
    phone_number_field = driver.find_element_by_name("phone")
    date_field = driver.find_element_by_name("Data_waznosc_prawo_jazdy")
    document_number_field = driver.find_element_by_name("Nr_dokumentu")
    password_field = driver.find_element_by_name("password1")
    password_confirm_field = driver.find_element_by_name("password2")
    submit_button = driver.find_element_by_name("submit")
    input_table = [email_field, username_field, first_name_field, last_name_field, phone_number_field, date_field, document_number_field, password_field, password_confirm_field]
    for j in range(len(input_table)):
        input_table[j].send_keys(input[j][i])
        submit_button.send_keys(Keys.RETURN)
    if driver.current_url == "http://127.0.0.1:8000/login/":
        print("Test udany")
    else:
        print("Test nieudany")
driver.quit()