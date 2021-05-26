from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers, login_admin
from os.path import abspath

driver = setup_drivers()
login_admin(driver)

input_add = [['Audi', 'Audi'], ['e', 'e'], ['2021', '2021'], ['30', '30'], ['5', '5'], ['testowy', 'testowy'], ['test2', 'test2'], ['test2', 'test2'], [abspath('car.png')]]
tests = [['T17', 'T18'], ['T15', 'T16']]
for i in range(2):
    print(f"\nTest: {tests[0][i]}")
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
        if not (j == 8 and i == 1):
            input_field[j].send_keys(input_add[j][i])
    submit_button.send_keys(Keys.RETURN)
    if driver.current_url == "http://127.0.0.1:8000/":
        print("Test udany")
    else:
        print("Test nieudany")

input_edit = [['Audi', 'Audi'], ['e', 'e'], ['2021', '2021'], ['30', '30'], ['5', '5'], ['testowy', 'testowy'], ['test', 'test'], ['test2', 'test2'], [abspath('car.png')]]
iterator = 0
while True:
    proper_url = f'http://127.0.0.1:8000/car/{iterator}/edit'
    print(f"\nSprawdzam link - ")
    print(proper_url)
    driver.get(proper_url)
    try:
        test = driver.find_element_by_name("nazwa")
        proper_url = f'http://127.0.0.1:8000/car/{iterator}/edit'
        print('Dobry link')
        break
    except:
        print('Zły link')
        iterator += 1

for i in range(2):
    print(f"\nTest: {tests[1][i]}")
    driver.get(proper_url)
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
    submit_button = driver.find_element_by_name("edit")
    input_field = [name_field, segment_field, prod_year_field, price_field, door_field, model_field, engine_field, additional_eq_field, image_field]
    for j in range(len(input_field)):
        if j not in (1, 5, 6, 7, 8):
            input_field[j].clear()
        if not (j == 8 and i == 1):
            input_field[j].send_keys(input_add[j][i])
    submit_button.send_keys(Keys.RETURN)
    if driver.current_url == "http://127.0.0.1:8000/":
        print("Test udany")
    else:
        print("Test nieudany")


driver.get("http://127.0.0.1:8000/logout/")
driver.quit()
