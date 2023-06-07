import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox('C:\\Users\\user\\Documents\\GitHub\\test-repository\\geckodriver')
driver.maximize_window()
driver.get("http://localhost/litecart/admin/")
time.sleep(2)
search_login = driver.find_element(By.NAME, "username")
search_login.send_keys('admin')
time.sleep(1)
search_password = driver.find_element(By.NAME, "password")
search_password.send_keys('admin')
time.sleep(1)
search_checkbox = driver.find_element(By.NAME, "remember_me").click()
time.sleep(2)
search_login = driver.find_element(By.NAME, "login").click()
time.sleep(3)
driver.quit()
if __name__ == '__main__':
    unittest.main()