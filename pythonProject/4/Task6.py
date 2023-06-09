from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0


if are_elements_present(driver, By.CSS_SELECTOR, "[id=app-]") is True:
    len_ = len(driver.find_elements(By.CSS_SELECTOR, "[id=app-]"))
    i=0
    while i < len_:
        temp = driver.find_elements(By.CSS_SELECTOR, "[id=app-]")
        temp[i].click()
        if is_element_present(driver, By.TAG_NAME, "h1") is True:
            print("Заголовок на странице N",i+1, " найден")
        else:
            print("Заголовок на странице N",i+1, " не найден")

        len__ = len(driver.find_elements(By.CSS_SELECTOR, "[id^=doc]"))
        j=0
        while j < len__:
            if is_element_present(driver, By.CSS_SELECTOR, "[id^=doc]") is True:
                temp = driver.find_elements(By.CSS_SELECTOR, "[id^=doc]")
                temp[j].click()
                if is_element_present(driver, By.TAG_NAME, "h1") is True:
                    print("Заголовок на странице N",i+1,".",j+1, " найден")
                else:
                    print("Заголовок на странице N",i+1,".",j+1, " не найден")
                j = j + 1
            else:
                print("Подзаголовков на странице №",i+1, "не найдено")
        i = i + 1

driver.quit()

