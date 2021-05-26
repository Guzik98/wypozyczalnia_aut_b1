from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers, login_admin

driver = setup_drivers()
login_admin(driver)
driver.get("http://127.0.0.1:8000/")
rezerwacje = driver.find_element_by_xpath('//*[text()=" Rezerwacje "]')
rezerwacje.click()
spis = driver.find_element_by_xpath('//*[text()="Spis rezerwacji"]')
spis.click()
print(f"\nTest: T43")
print("Test udany")
input_table = [['20032022', '20032021'], []]
tests = ["T47", "T48"]
driver.get("http://127.0.0.1:8000/wyswietlanie_rezerwacji/")
for i in range(2):
    print(f"\nTest: {tests[i]}")
    odbior = driver.find_element_by_name("data_odbioru")
    zwrot = driver.find_element_by_name("data_zwrotu")
    submit_button = driver.find_element_by_name("filtruj")
    odbior.send_keys(input_table[i])
    submit_button.click()
    if driver.find_elements_by_xpath("//*[contains(text(), 'Wypożyczone auto')]"):
        print("Test udany")
    else:
        print("Test nieudany LUB brak rezerwacji")

driver.get("http://127.0.0.1:8000/logout/")
driver.quit()