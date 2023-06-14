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

def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False

if are_elements_present(driver,By.CLASS_NAME, "product") is True:
 temp = driver.find_elements(By.CLASS_NAME, "product")
 i=0
 while i < len(temp):
        if len(temp[i].find_elements(By.CLASS_NAME, "sticker")) > 1:
                print("У товара стикеров больше, чем один ")
        if len(temp[i].find_elements(By.CLASS_NAME, "sticker")) == 1:
            print("У товара номер",i,"ровно один стикер")
        else:
            print("У товара нет стикеров ")
        i=i+1

driver.quit()
