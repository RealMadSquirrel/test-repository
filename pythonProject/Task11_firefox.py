import re
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from faker import Faker

fake = Faker()



class test_11(unittest.TestCase):
    """Авторизуемся и вводим код"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(capabilities={"marionette": False})
        cls.driver.maximize_window()
        cls.driver.get("http://localhost/litecart/en/create_account")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_new_user(self):
        tax_id = self.driver.find_element(By.XPATH, "//*[@name='tax_id']")
        tax_id.send_keys('User')

        tax_id = self.driver.find_element(By.XPATH, "//*[@name='company']")
        tax_id.send_keys('Anderson')

        firstname = self.driver.find_element(By.XPATH, "//*[@name='firstname']")
        firstname.send_keys('Olga')

        lastname = self.driver.find_element(By.XPATH, "//*[@name='lastname']")
        lastname.send_keys('Belova')

        address1 = self.driver.find_element(By.XPATH, "//*[@name='address1']")
        address1.send_keys('Tverskaya 15')

        postcode = self.driver.find_element(By.XPATH, "//*[@name='postcode']")
        postcode.send_keys('12345')

        city = self.driver.find_element(By.XPATH, "//*[@name='city']")
        city.send_keys('NY')

        country = self.driver.find_element(By.XPATH, "//*[@role='presentation']")
        country.click()
        country_tab = self.driver.find_element(By.CLASS_NAME, "select2-results__options")
        temp = country_tab.find_elements(By.TAG_NAME, "li")
        l = 0
        while l < len(temp):
            us = temp[l].text
            if us == "United States":
                temp[l].click()
                break
            l = l + 1
        time.sleep(1)
        zone = self.driver.find_element(By.XPATH, "//*[@name='zone_code']")
        zone.find_element(By.XPATH, "//*[@value='AK']").click()

        email = self.driver.find_element(By.XPATH, "//*[@name='email']")
        temp = fake.email()
        email.send_keys(temp)

        phone = self.driver.find_element(By.XPATH, "//*[@name='phone']")
        phone.send_keys('+123456789')

        pword = "admin"
        password = self.driver.find_element(By.XPATH, "//*[@name='password']")
        password.send_keys(pword)

        confirmed_password = self.driver.find_element(By.XPATH, "//*[@name='confirmed_password']")
        confirmed_password.send_keys(pword)
        time.sleep(2)
        create_account = self.driver.find_element(By.XPATH, "//*[@name='create_account']")
        create_account.click()
        time.sleep(2)
        create_account = self.driver.find_element(By.XPATH, "//*[@id='box-account']/div/ul/li[4]/a")
        create_account.click()

        self.driver.find_element(By.XPATH, "//*[@name='email']").send_keys(temp)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@name='password']").send_keys(pword)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@name='login']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='box-account']/div/ul/li[4]/a").click()



if __name__ == '__main__':
    unittest.main()