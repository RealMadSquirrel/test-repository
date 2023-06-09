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

#Appearence
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=appearance&doc=template']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:
    driver.find_element(By.XPATH, "//*[@id='doc-template']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-logotype']/a").click()
else:
    print("Заголовок не найден")

#Catalog
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=catalog&doc=catalog']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:
    driver.find_element(By.XPATH,"//*[@id='doc-catalog']/a").click()
    driver.find_element(By.XPATH,"//*[@id='doc-product_groups']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-option_groups']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-manufacturers']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-suppliers']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-delivery_statuses']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-sold_out_statuses']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-quantity_units']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-csv']/a").click()
else:
    print("Заголовок не найден")
#Countries
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=countries&doc=countries']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:
    print("Подпунктов нет")
else:
    print("Заголовок не найден")

#Currencies
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=currencies&doc=currencies']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:
    print("Подпунктов нет")
else:
    print("Заголовок не найден")

#Customers
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=customers&doc=customers']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:
    driver.find_element(By.XPATH,"//*[@id='doc-customers']/a").click()
    driver.find_element(By.XPATH,"//*[@id='doc-csv']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-newsletter']/a").click()

else:
    print("Заголовок не найден")

#Geo Zones
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:
    print("Подпунктов нет")
else:
    print("Заголовок не найден")

#Languages
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=languages&doc=languages']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:

    driver.find_element(By.XPATH,"//*[@id='doc-languages']/a").click()
    driver.find_element(By.XPATH,"//*[@id='doc-storage_encoding']/a").click()

else:
    print("Заголовок не найден")

#Modules
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=modules&doc=jobs']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:
    driver.find_element(By.XPATH,"//*[@id='doc-jobs']/a").click()
    driver.find_element(By.XPATH,"//*[@id='doc-customer']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-shipping']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-payment']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-order_total']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-order_success']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-order_action']/a").click()

else:
    print("Заголовок не найден")
#Orders
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=orders&doc=orders']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:

    driver.find_element(By.XPATH,"//*[@id='doc-orders']/a").click()
    driver.find_element(By.XPATH,"//*[@id='doc-order_statuses']/a").click()

else:
    print("Заголовок не найден")

#Pages
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=pages&doc=pages']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:
    print("Подпунктов нет")
else:
    print("Заголовок не найден")
#Reports
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=reports&doc=monthly_sales']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:

    driver.find_element(By.XPATH,"//*[@id='doc-monthly_sales']/a").click()
    driver.find_element(By.XPATH,"//*[@id='doc-most_sold_products']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-most_shopping_customers']/a").click()

else:
    print("Заголовок не найден")

#Modules
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=settings&doc=store_info']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:
    driver.find_element(By.XPATH,"//*[@id='doc-store_info']/a").click()
    driver.find_element(By.XPATH,"//*[@id='doc-general']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-listings']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-images']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-checkout']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-advanced']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-security']/a").click()

else:
    print("Заголовок не найден")

#Slides
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=slides&doc=slides']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:
    print("Подпунктов нет")
else:
    print("Заголовок не найден")

#Tax
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=tax&doc=tax_classes']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:

    driver.find_element(By.XPATH,"//*[@id='doc-tax_classes']/a").click()
    driver.find_element(By.XPATH,"//*[@id='doc-tax_rates']/a").click()

else:
    print("Заголовок не найден")

# Translations
driver.find_element(By.XPATH, "//*[@href='http://localhost/litecart/admin/?app=translations&doc=search']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:

    driver.find_element(By.XPATH, "//*[@id='doc-search']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-scan']/a").click()
    driver.find_element(By.XPATH, "//*[@id='doc-csv']/a").click()

else:
    print("Заголовок не найден")

#users
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=users&doc=users']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:
    print("Подпунктов нет")
else:
    print("Заголовок не найден")

#vQmods
driver.find_element(By.XPATH,"//*[@href='http://localhost/litecart/admin/?app=vqmods&doc=vqmods']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//*[@id='content']/h1") is not None:

    driver.find_element(By.XPATH,"//*[@id='doc-vqmods']/a").click()


else:
    print("Заголовок не найден")

driver.quit()
if __name__ == '__main__':
    unittest.main()