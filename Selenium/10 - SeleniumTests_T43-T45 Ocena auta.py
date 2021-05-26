from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers, login_user2
from os.path import abspath

driver = setup_drivers()
login_user2(driver)
input_list = [['1', '2', '2'],
              ['1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Gooooooooooooooooood', 'zaqxswed']]
iterator = 0
while True:
    proper_url = f'http://127.0.0.1:8000/car/{iterator}/rate'
    print(f"\nSprawdzam link - ")
    print(proper_url)
    driver.get(proper_url)
    try:
        test = driver.find_element_by_name("rate")
        proper_url = f'http://127.0.0.1:8000/car/{iterator}/rate'
        print('Dobry link')
        break
    except:
        print('Zły link')
        iterator += 1

tests = ["T25", "T26", "T27"]
for i in range(3):
    driver.get(proper_url)
    print(f"\nTest: {tests[i]}")
    text_field = driver.find_element_by_name("text")
    rating_field = driver.find_element_by_name("rate")
    submit_button = driver.find_element_by_name('submit')
    rating_field.click()
    rating_field.send_keys(input_list[0][i])
    text_field.send_keys(input_list[1][i])
    submit_button.click()
    if driver.current_url == f'http://127.0.0.1:8000/car/{iterator}/':
        print("Test udany")
    else:
        print("Test nieudany")
driver.get("http://127.0.0.1:8000/logout/")
driver.quit()