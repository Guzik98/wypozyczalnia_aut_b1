from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers, login_user, login_user2

driver = setup_drivers()
login_user(driver)
input = [["ktośtam@wp.pl", "ktostam2@wp.pl", "ktostam@wp.pl", "ktostam@wp.pl", "ktostam2@wp.pl"],
["Michał", "Michał", "Andrzej", "Michał", "Michał"],
["Kowalski", "Kowalski", "Kowalski", "Kowalski", "Kowalski"],
["+48509993630", "0124234", "+48509993630", "+48509993630", "+48660124234"],
["12032024", "12", "21052020", "21052020", "12032024"],
["544448481", "CAD212344", "54444848", "5444484812", "CAD212344"]]
test = ['T11', 'T12', 'T13', 'T14', 'T10']
for i in range(5):
    print(f"\nTest  {test[i]}")
    driver.get("http://127.0.0.1:8000/edit_account_redirect/")
    email_field = driver.find_element_by_name("email")
    fname_field = driver.find_element_by_name("first_name")
    lname_field = driver.find_element_by_name("last_name")
    phone_number_field = driver.find_element_by_name("phone")
    expire_date_field = driver.find_element_by_name("Data_waznosc_prawo_jazdy")
    document_number_field = driver.find_element_by_name("Nr_dokumentu")
    input_table = [email_field, fname_field, lname_field, phone_number_field, expire_date_field, document_number_field]
    submit_button = driver.find_element_by_name("submit")
    for j in range(len(input_table)):
        input_table[j].clear()
        input_table[j].send_keys(input[j][i])
    submit_button.send_keys(Keys.RETURN)
    if driver.current_url == "http://127.0.0.1:8000/":
        print("Test udany")
        driver.get("http://127.0.0.1:8000/login/")
        login_user2(driver)
    else:
        print("Test nieudany")
driver.quit()
