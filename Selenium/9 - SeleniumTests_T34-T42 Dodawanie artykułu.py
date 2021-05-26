from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from SeleniumLoginAdmin import login_admin, setup_drivers

driver = setup_drivers()
login_admin(driver)
driver.get("http://127.0.0.1:8000/wyswietlanieArtykulow/newArticle/")

#Dane do wprowadzenia
title_inputs = ["test", "", "adadadfsa", "testgdfsgfdsggg"]
content_inputs = ["Treść artykułu", "Treść artykułu", "Treść", "zaqwsxcde"]
test = ['T34', 'T35', 'T36', 'T37']
for i in range(4):
    print(f"\nTest  {test[i]}")
    #Pola do wprowadzania danych
    title_field = driver.find_element_by_name("title")
    content_field = driver.find_element_by_name("text")
    image_field = driver.find_element_by_name("zdjecie")
    submit_button = driver.find_element_by_name("submit")

    title_field.send_keys(title_inputs[i])
    content_field.send_keys(content_inputs[i])
    submit_button.send_keys(Keys.RETURN)
    if driver.current_url == "http://127.0.0.1:8000/wyswietlanieArtykulow/":
        print("Test udany")
    else:
        print("Test nieudany")

    driver.get("http://127.0.0.1:8000/wyswietlanieArtykulow/newArticle/")

too_long_title, too_long_input, almost_proper_title, proper_title, proper_input  = "", "", "Hello world!", "Mycie aut", "Testowa treść"
for i in range(160):
    if i < 40:
        too_long_title+="a"
    too_long_input+="a"

iterator = 0
titles  = ["", almost_proper_title, almost_proper_title, proper_title]
inputs = [too_long_input, too_long_input, too_long_input, proper_input]
while True:
    proper_url = f'http://127.0.0.1:8000/wyswietlanieArtykulow/article/{iterator}/edit'
    print(f"\nSprawdzam link - ")
    print(proper_url)
    driver.get(proper_url)
    try:
        test = driver.find_element_by_name("title")
        proper_url = f'http://127.0.0.1:8000/wyswietlanieArtykulow/article/{iterator}'
        print('Dobry link')
        break
    except:
        print('Zły link')
        iterator += 1
test = ['T39', 'T40', 'T41', 'T42']
for i in range(4):
    print(f"\nTest  {test[i]}")
    driver.get(proper_url + "/edit")
    title_field = driver.find_element_by_name("title")
    content_field =  driver.find_element_by_name("text")
    submit_button = driver.find_element_by_name("edit")

    title_field.send_keys(titles[i])
    content_field.send_keys(inputs[i])
    submit_button.send_keys(Keys.RETURN)
    if driver.current_url == "http://127.0.0.1:8000/wyswietlanieArtykulow/":
        print("Test udany")
    else:
        print("Test nieudany")
    #Trzeba zmieniać index artykułu do edycji na bieżący artykuł (taki który istnieje)
    driver.get(proper_url + "/edit")


print("\nTest T38")
#Trzeba zmieniać index artykułu do usunięcia na bieżący artykuł (taki który istnieje)
driver.get(proper_url + "/delete")
submit_button = driver.find_element_by_name("delete")
submit_button.send_keys(Keys.RETURN)
if driver.current_url == "http://127.0.0.1:8000/wyswietlanieArtykulow/":
    print("Test udany")
else:
    print("Test nieudany")


driver.get("http://127.0.0.1:8000/logout/")
driver.quit()
