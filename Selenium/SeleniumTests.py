from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from SeleniumLogin import login, setup_drivers

driver = setup_drivers()
login(driver)
driver.get("http://127.0.0.1:8000/wyswietlanieArtykulow/newArticle/")

#Dane do wprowadzenia
title_inputs = ["test", "", "adadadfsa", "testgdfsgfdsggg"]
image_input = "./Selenium/image_test_article.jpg"
content_inputs = ["Treść artykułu", "Treść artykułu", "Treść", "zaqwsxcde"]
print("\nTesty Dodawania")
for i in range(4):
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

print("\nTesty Edycji")
too_long_title, too_long_input, almost_proper_title, proper_title, proper_input  = "", "", "Hello world!", "Mycie aut", "Testowa treść"
for i in range(160):
    if i < 40:
        too_long_title+="a"
    too_long_input+="a"

titles  = ["", almost_proper_title, almost_proper_title, proper_title]
inputs = [too_long_input, too_long_input, too_long_input, proper_input]


for i in range(4):
    #Trzeba zmieniać index artykułu do edycji na bieżący artykuł (taki który istnieje)
    driver.get("http://127.0.0.1:8000/wyswietlanieArtykulow/article/43/edit")
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
    driver.get("http://127.0.0.1:8000/wyswietlanieArtykulow/article/43/edit")


print("\nTest usuwania")
#Trzeba zmieniać index artykułu do usunięcia na bieżący artykuł (taki który istnieje)
driver.get("http://127.0.0.1:8000/wyswietlanieArtykulow/article/43/delete")
submit_button = driver.find_element_by_name("delete")
submit_button.send_keys(Keys.RETURN)
if driver.current_url == "http://127.0.0.1:8000/wyswietlanieArtykulow/":
    print("Test udany")
else:
    print("Test nieudany")


driver.get("http://127.0.0.1:8000/logout/")
