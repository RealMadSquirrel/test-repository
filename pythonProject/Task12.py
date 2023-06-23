import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os.path

class test_12(unittest.TestCase):
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

    def test_add_new_product(self):
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
        self.driver.find_element(By.XPATH, "//*[@id='content']/div[1]/a[2]").click()


    def test_general(self):
        self.driver.find_element(By.TAG_NAME,"label").find_element(By.XPATH, "//*[@value='1']").click()
        self.driver.find_element(By.XPATH, "//input[@name='name[en]']").send_keys("Teddy")
        self.driver.find_element(By.XPATH, "//input[@name='code']").send_keys("567")
        self.driver.find_element(By.XPATH, "//input[@value='1-3']").click()
        quantity = self.driver.find_element(By.XPATH, "//input[@name='quantity']")
        quantity.clear()
        quantity.send_keys("5")
        path = os.path.abspath("teddy.png")
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(path)
        self.driver.find_element(By.XPATH, "//input[@name='date_valid_from']").send_keys(Keys.HOME + "01.01.2023")
        self.driver.find_element(By.XPATH, "//input[@name='date_valid_to']").send_keys(Keys.HOME + "01.01.2024")


    def test_information(self):
        self.driver.find_element(By.XPATH, "//*[@id='content']/form/div/ul/li[2]/a").click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='manufacturer_id']")))
        self.driver.find_element(By.XPATH, "//select[@name='manufacturer_id']").find_element(By.XPATH, "option[@value='1']").click()
        self.driver.find_element(By.XPATH, "//input[@name='keywords']").send_keys("Bear")
        self.driver.find_element(By.XPATH, "//input[@name='short_description[en]']").send_keys("Сhildren's toy")
        self.driver.find_element(By.XPATH, "//div[@class='trumbowyg-editor']").send_keys("The teddy bear is one of the most popular stuffed toys since the 20th century, which has become a symbol of a carefree happy childhood. It was at this time that the mass production of soft toys in general and, of course, teddy bears, which are most in demand among children, was launched.")
        self.driver.find_element(By.XPATH, "//input[@name='head_title[en]']").send_keys("Toy")
        self.driver.find_element(By.XPATH, "//input[@name='meta_description[en]']").send_keys("Toy")


    def test_prices(self):
        self.driver.find_element(By.XPATH, "//*[@id='content']/form/div/ul/li[4]/a").click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='purchase_price']")))
        price = self.driver.find_element(By.XPATH, "//input[@name='purchase_price']")
        price.clear()
        price.send_keys("1550")
        self.driver.find_element(By.XPATH, "//select[@name='purchase_price_currency_code']").find_element(By.XPATH,
                                                                                             "option[@value='USD']").click()
        price1 = self.driver.find_element(By.XPATH, "//input[@name='prices[USD]']")
        price1.clear()
        price1.send_keys("1550")

        price2 = self.driver.find_element(By.XPATH, "//input[@name='prices[EUR]']")
        price2.clear()
        price2.send_keys("1550")

        self.driver.find_element(By.XPATH, "//button[@value='Save']").click()
        temp = self.driver.find_element(By.CLASS_NAME, "dataTable").find_elements(By.CLASS_NAME, "row")
        len_ = len(temp)
        i = 0
        while i < len_:
            if temp[i].text == "Teddy":
                print("товар добавлен")
            i = i + 1





if __name__ == '__main__':
    unittest.main()