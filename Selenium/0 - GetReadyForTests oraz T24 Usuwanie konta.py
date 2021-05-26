from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers, login_admin
driver = setup_drivers()
login_admin(driver)
try:
    print("Test T24")
    driver.get("http://127.0.0.1:8000/admin/users/account/")
    konto = driver.find_element_by_xpath('//*[text()="ktostam@wp.pl"]')
    konto.click()
    usun_konto = driver.find_element_by_xpath('//*[text()="Usuń"]')
    usun_konto.click()
    usun_konto_confirm = driver.find_element_by_xpath("//input[@type='submit']")
    usun_konto_confirm.click()
    print("Test udany  (konto ktostam@wp.pl istnieje)")
except:
    print("Test nieudany (konto ktostam@wp.pl nie istnieje)")
    pass
try:
    print("Test T24")
    driver.get("http://127.0.0.1:8000/admin/users/account/")
    konto = driver.find_element_by_xpath('//*[text()="ktostam2@wp.pl"]')
    konto.click()
    usun_konto = driver.find_element_by_xpath('//*[text()="Usuń"]')
    usun_konto.click()
    usun_konto_confirm = driver.find_element_by_xpath("//input[@type='submit']")
    usun_konto_confirm.click()
    print("Test udany  (konto ktostam2@wp.pl istnieje)")
except:
    print("Test nieudany (konto ktostam2@wp.pl nie istnieje)")
    pass

try:
    driver.get("http://127.0.0.1:8000/admin/wypozyczalnia/segment/")
    segment = driver.find_element_by_xpath('//*[text()="E"]')
    segment.click()
    usun_segment = driver.find_element_by_xpath('//*[text()="Usuń"]')
    usun_segment.click()
    usun_segment_confirm = driver.find_element_by_xpath("//input[@type='submit']")
    usun_segment_confirm.click()

except:
    pass

try:
    print("Test T24")
    driver.get("http://127.0.0.1:8000/admin/users/account/")
    konto = driver.find_element_by_xpath('//*[text()="pracownik@wp.pl"]')
    konto.click()
    usun_konto = driver.find_element_by_xpath('//*[text()="Usuń"]')
    usun_konto.click()
    usun_konto_confirm = driver.find_element_by_xpath("//input[@type='submit']")
    usun_konto_confirm.click()
    print("Test udany  (konto pracownik@wp.pl istnieje)")
except:
    print("Test nieudany (konto pracownik@wp.pl nie istnieje)")
    pass


driver.get("http://127.0.0.1:8000/logout/")
driver.quit()
print("Testy gotowe")