import unittest
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://localhost/litecart/admin/")
search_login = driver.find_element(By.NAME, "username")
search_login.send_keys('admin')
search_password = driver.find_element(By.NAME, "password")
search_password.send_keys('admin')
search_checkbox = driver.find_element(By.NAME, "remember_me").click()
search_login = driver.find_element(By.NAME, "login").click()
driver.find_element(By.XPATH, "//*[@id='sidebar']/div[2]/a[1]").click()
time.sleep(2)

def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0
are_elements_present(driver, By.CSS_SELECTOR, "[class^=sticker]")

list_a = driver.find_elements(By.CSS_SELECTOR, "[class^=sticker]")
for i in list_a:
    if i is not None:
     print("Cтикер у элемента номер",list_a.index(i),"есть")
driver.quit()
if __name__ == '__main__':
    unittest.main()