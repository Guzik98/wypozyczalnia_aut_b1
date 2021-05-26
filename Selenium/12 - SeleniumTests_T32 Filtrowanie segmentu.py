from selenium.webdriver.common.keys import Keys
from SeleniumLoginAdmin import setup_drivers, login_user2

driver = setup_drivers()
login_user2(driver)
driver.get("http://127.0.0.1:8000/")
segment_szukany = driver.find_element_by_name("selected_segment")
segment_szukany.click()
print("Test T32")
segment_szukany.send_keys("B")
filtrowanie = driver.find_element_by_xpath('//*[text()="Filtruj"]')
filtrowanie.click()
if driver.current_url == f'http://127.0.0.1:8000/?selected_segment=2':
    print("Test udany")
else:
    print("Test nieudany")
driver.get("http://127.0.0.1:8000/logout/")
driver.quit()