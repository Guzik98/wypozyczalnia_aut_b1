from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers, login_admin

driver = setup_drivers()
login_admin(driver)
iterator = 0
while True:
    proper_url = f'http://127.0.0.1:8000/rezerwacja/{iterator}/'
    print(f"\nSprawdzam link - ")
    print(proper_url)
    driver.get(proper_url)
    try:
        test = driver.find_element_by_name("data_zwrotu")
        proper_url = f'http://127.0.0.1:8000/rezerwacja/{iterator}/'
        print('Dobry link')
        break
    except:
        print('Zły link')
        iterator += 1

input_table = [['22052019', '22112021', '22112021'],
               ['1950', '1950', '1950'],
               ['24112021', '24112019', '24112021'],
               ['1950', '1950', '1950']]
testy = ['T26', 'T27', 'T25']
for i in range(3):
    print(f"\nTest: {testy[i]}")
    driver.get(proper_url)
    odbior = driver.find_element_by_name("data_odbioru")
    odbior_h = driver.find_element_by_name("godzina_odbioru")
    zwrot = driver.find_element_by_name("data_zwrotu")
    zwrot_h = driver.find_element_by_name("godzina_zwrotu")
    odbior_m = driver.find_element_by_name("miejsce_odbioru")
    zwrot_m = driver.find_element_by_name("miejsce_zwrotu")
    submit_button = driver.find_element_by_name("submit")
    input_fields = [odbior, odbior_h, zwrot, zwrot_h]
    zwrot_m.send_keys("Gdańsk")
    odbior_m.send_keys("Gdańsk")
    for j in range(len(input_fields)):
        input_fields[j].send_keys(input_table[j][i])
    submit_button.click()
    if driver.current_url == "http://127.0.0.1:8000/":
        print("Test udany")
    else:
        print("Test nieudany")

driver.get("http://127.0.0.1:8000/logout/")
driver.quit()