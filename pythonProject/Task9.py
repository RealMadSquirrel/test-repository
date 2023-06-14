import time
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
search_login = driver.find_element(By.NAME, "username")
search_login.send_keys('admin')
search_password = driver.find_element(By.NAME, "password")
search_password.send_keys('admin')
search_checkbox = driver.find_element(By.NAME, "remember_me").click()
search_login = driver.find_element(By.NAME, "login").click()
time.sleep(2)

def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False

def test_alf_sort(list):

        m = 0
        while m < len(list) - 1:
            if list[m] > list[m + 1] is True:
              raise Exception("На этом элементе - ", list[m], "сортировка в алфавитном порядке слетела")
            m = m + 1
        print("Тест на сортировку в алфавитном порядке пройден")


table = driver.find_element(By.TAG_NAME, "table")
row = table.find_elements(By.CLASS_NAME, "row")
list_zones = []

if are_elements_present(table, By.CLASS_NAME, "row") is True:
    len_ = len(row)
    i = 0
    while i < len_:
        temp = driver.find_elements(By.CLASS_NAME, "row")
        zones = temp[i].find_element(By.XPATH, "td[3]/a")
        zones.click()
        name_zones = driver.find_elements(By.XPATH, "//*[@id='table-zones']/tbody/tr/td[3]/select")
        l = 0
        while l < len(name_zones):
            pp = name_zones[l].find_element(By.XPATH, "option[@selected='selected']")
            list_zones.append(pp.text)
            print(pp.text)
            l = l + 1
        test_alf_sort(list_zones)
        driver.back()
        i = i + 1
driver.quit()