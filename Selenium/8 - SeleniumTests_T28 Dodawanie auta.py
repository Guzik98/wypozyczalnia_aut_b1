from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers, login_admin
from os.path import abspath

driver = setup_drivers()
login_admin(driver)

input_add = ['Audi', 'e', '2021', '30',  '5', 'testowy', 'test2', 'test2', abspath('car.png')]
tests = ['T28']

print(f"\nTest: {tests[0]}")
driver.get('http://127.0.0.1:8000')
driver.get('http://127.0.0.1:8000/newCar/')
name_field = driver.find_element_by_name("nazwa")
segment_field = driver.find_element_by_name("segment")
prod_year_field = driver.find_element_by_name("rok_produkcji")
price_field = driver.find_element_by_name("cena_za_godzine")
dost_checkbox = driver.find_element_by_name("dostepnosc")
klim_checkbox = driver.find_element_by_name("klimatyzacja")
door_field = driver.find_element_by_name('ilosc_drzwi')
model_field = driver.find_element_by_name("model")
engine_field = driver.find_element_by_name("silnik")
additional_eq_field = driver.find_element_by_name("opcjonalne_wyposazenie")
image_field = driver.find_element_by_name("zdjecie")
submit_button = driver.find_element_by_name("submit")
input_field = [name_field, segment_field, prod_year_field, price_field, door_field, model_field, engine_field, additional_eq_field, image_field]
for j in range(len(input_field)):
    input_field[j].send_keys(input_add[j])
submit_button.send_keys(Keys.RETURN)
if driver.current_url == "http://127.0.0.1:8000/":
    print("Test udany")
else:
    print("Test nieudany")

driver.get("http://127.0.0.1:8000/logout/")
driver.quit()
