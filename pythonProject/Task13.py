import time
import unittest

from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False


def check_cat(quantity, quantity_new):
    if int(quantity) + 1 == int(quantity_new):
        print("Корзина обновилась - количество элементов", quantity_new)
        return True
    else:
        print("Корзина не обновилась - ", quantity_new)
        return False




class test_13(unittest.TestCase):
    """Авторизуемся и вводим код"""

    @classmethod
    def setUpClass(cls):
        cls.options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.maximize_window()
        cls.driver.get("http://localhost/litecart/en/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_new_product(self):
        search_product = self.driver.find_element(By.XPATH, "//*[@id='box-most-popular']/div/ul")
        search_product.find_element(By.XPATH, "li[1]").click()
        add_to_cat = self.driver.find_element(By.XPATH, "//button[@name='add_cart_product']")
        quantity = self.driver.find_element(By.CLASS_NAME, "quantity").text
        if is_element_present(self.driver, By.XPATH, "//select[@required='required']") is True:
            self.driver.find_element(By.XPATH, "//option[@value='Small']").click()
            add_to_cat.click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(int(quantity) + 1)))
            quantity_new = self.driver.find_element(By.CLASS_NAME, "quantity").text
            check_cat(quantity, quantity_new)
            self.driver.back()
        else:
            add_to_cat.click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(int(quantity) + 1)))
            quantity_new = self.driver.find_element(By.CLASS_NAME, "quantity").text
            check_cat(quantity, quantity_new)
            self.driver.back()

        search_product = self.driver.find_element(By.XPATH, "//*[@id='box-most-popular']/div/ul")
        search_product.find_element(By.XPATH, "li[1]").click()
        add_to_cat = self.driver.find_element(By.XPATH, "//button[@name='add_cart_product']")
        quantity = self.driver.find_element(By.CLASS_NAME, "quantity").text
        if is_element_present(self.driver, By.XPATH, "//select[@required='required']") is True:
            self.driver.find_element(By.XPATH, "//option[@value='Small']").click()
            add_to_cat.click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(int(quantity) + 1)))
            quantity_new = self.driver.find_element(By.CLASS_NAME, "quantity").text
            check_cat(quantity, quantity_new)
            self.driver.back()
        else:
            add_to_cat.click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(int(quantity) + 1)))
            quantity_new = self.driver.find_element(By.CLASS_NAME, "quantity").text
            check_cat(quantity, quantity_new)
            self.driver.back()

        search_product = self.driver.find_element(By.XPATH, "//*[@id='box-most-popular']/div/ul")
        search_product.find_element(By.XPATH, "li[1]").click()
        add_to_cat = self.driver.find_element(By.XPATH, "//button[@name='add_cart_product']")
        quantity = self.driver.find_element(By.CLASS_NAME, "quantity").text
        if is_element_present(self.driver, By.XPATH, "//select[@required='required']") is True:
            self.driver.find_element(By.XPATH, "//option[@value='Small']").click()
            add_to_cat.click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(int(quantity) + 1)))
            quantity_new = self.driver.find_element(By.CLASS_NAME, "quantity").text
            check_cat(quantity, quantity_new)
            self.driver.back()
        else:
            add_to_cat.click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(int(quantity) + 1)))
            quantity_new = self.driver.find_element(By.CLASS_NAME, "quantity").text
            check_cat(quantity, quantity_new)
            self.driver.back()

    def test_delete_products(self):
        checkout = self.driver.find_element(By.XPATH, "//*[@id='cart']/a[3]")
        checkout.click()
        item = self.driver.find_elements(By.XPATH, "//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[2]")
        len_=len(item)
        i=0
        while i <=len_-3:
            if is_element_present(self.driver, By.CLASS_NAME, "shortcut") is True:
                shortcut = self.driver.find_elements(By.CLASS_NAME, "shortcut")
                shortcut[i].click()
                wait = WebDriverWait(self.driver, 10)
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='remove_cart_item']")))
                    self.driver.find_element(By.XPATH, "//button[@name='remove_cart_item']").click()
                    print("Удалили товар")
                    wait.until(EC.staleness_of(item[i]))
                    item = self.driver.find_elements(By.XPATH,
                                                     "//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[2]")
                except TimeoutException:
                    pass
            else:
                wait = WebDriverWait(self.driver, 10)  # seconds
                try:
                    wait.until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@name='remove_cart_item']")))
                    self.driver.find_element(By.XPATH, "//button[@name='remove_cart_item']").click()
                    print("Удалили последний товар")
                    wait.until(
                            EC.presence_of_element_located((By.XPATH, "//*[@id='checkout-cart-wrapper']/p[1]/em")))
                    print("Корзина пуста")
                    break

                except TimeoutException:
                    print("Remove not clickable")
                    pass


if __name__ == '__main__':
    unittest.main()