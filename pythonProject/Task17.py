from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os.path
from faker import Faker

class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)
    def after_find(self, by, value, driver):
        print(by, value, "found")
    def on_exception(self, exception, driver):
        print(exception)

class test_17(unittest.TestCase):
    """Авторизуемся и вводим код"""

    @classmethod
    def setUpClass(cls):
        cls.options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.maximize_window()
        cls.driver.get("http://localhost/litecart/admin")



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_logs(self):
        search_login = self.driver.find_element(By.NAME, "username")
        search_login.send_keys('admin')
        search_password = self.driver.find_element(By.NAME, "password")
        search_password.send_keys('admin')
        self.driver.find_element(By.NAME, "remember_me").click()
        self.driver.find_element(By.NAME, "login").click()
        len_ = len(self.driver.find_elements(By.CSS_SELECTOR, "[id=app-]"))
        i = 0
        while i < len_:
            temp = self.driver.find_elements(By.CSS_SELECTOR, "[id=app-]")
            if temp[i].text == "Catalog":
                temp[i].click()

            i = i + 1

        self.driver.find_element(By.XPATH, "//*[@id='content']/form/table/tbody/tr[3]/td[3]/a").click()

        dataTable = self.driver.find_element(By.XPATH, "//*[@id='content']/form/table/tbody")
        links = dataTable.find_elements(By.XPATH, "//a[@title='Edit']")
        j = 0
        len_ = len(links)
        while j < len_:
            dataTable = self.driver.find_element(By.XPATH, "//*[@id='content']/form/table/tbody")
            links = dataTable.find_elements(By.XPATH, "//a[@title='Edit']")
            q = links[j].get_attribute('href')
            if links[j].get_attribute('href').find("product_id") > -1:
                links[j].click()
                try:
                    for l in self.driver.get_log("browser"):
                        print(l)
                except:
                    print("Сообщений в логе браузера не появилось")
                self.driver.back()

            j = j + 1

    if __name__ == '__main__':
        unittest.main()