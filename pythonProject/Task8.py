import time
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
search_login = driver.find_element(By.NAME, "username")
search_login.send_keys('admin')
search_password = driver.find_element(By.NAME, "password")
search_password.send_keys('admin')
search_checkbox = driver.find_element(By.NAME, "remember_me").click()
search_login = driver.find_element(By.NAME, "login").click()


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
list_country = []
list_zones = []


# a
if are_elements_present(table, By.CLASS_NAME, "row") is True:
    len_ = len(row)
    i = 0
    while i < len_:
        temp = driver.find_elements(By.CLASS_NAME, "row")
        href = temp[i].find_elements(By.TAG_NAME, "a")
        zones = temp[i].find_element(By.XPATH, "td[6]")
        j = 0
        while j < len(href):
            if len(href[j].text) > 0:
                list_country.append(href[j].text)
                print(href[j].text)
            j = j + 1

        i = i + 1
test_alf_sort(list_country)

# b
if are_elements_present(driver, By.CLASS_NAME, "row") is True:
    f=0
    while f < len_:
        temp = driver.find_elements(By.CLASS_NAME, "row")
        zones = temp[f].find_element(By.XPATH, "td[6]")
        href = temp[f].find_elements(By.TAG_NAME, "a")
        a = zones.get_attribute("outerText")
        if zones.get_attribute("outerText") != "0":
            a = temp[f].find_element(By.XPATH, "td[5]/a")
            a.click()
            table_zones = driver.find_element(By.ID, "table-zones")
            name_zones = table_zones.find_elements(By.XPATH, "tbody/tr/td[3]")
            l = 0
            while l < len(name_zones):
                if len(name_zones[l].text) > 0:
                    list_zones.append(name_zones[l].text)
                    print(name_zones[l].text)
                l = l + 1
            test_alf_sort(list_zones)
            driver.back()

        f = f + 1

driver.quit()
