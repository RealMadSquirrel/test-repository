import re
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class test_14(unittest.TestCase):
    """Авторизуемся и вводим код"""

    @classmethod
    def setUpClass(cls):
        cls.options = webdriver.ChromeOptions()
        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.maximize_window()
        cls.driver.get("http://localhost/litecart/admin/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_links(self):
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
            if temp[i].text == "Countries":
                temp[i].click()
            i = i + 1
        dataTable = self.driver.find_element(By.CLASS_NAME, "dataTable")
        temp = self.driver.find_elements(By.CLASS_NAME, "row")
        href = temp[0].find_elements(By.TAG_NAME, "a")
        href[0].click()
        links = self.driver.find_elements(By.XPATH, "//*[@id='content']/form/table[1]/tbody/tr/td/a[@target='_blank']")
        i = 0
        len_ = len(links)
        while i < len_:
            original_window = self.driver.current_window_handle
            existing_windows = self.driver.window_handles
            links[i].click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.number_of_windows_to_be(2))
            windows_open = self.driver.window_handles
            for j in range(len(windows_open)):
                if windows_open[j] != original_window:
                    self.driver.switch_to.window(windows_open[j])
                    wait = WebDriverWait(self.driver, 10)  # seconds
                    wait.until(EC.visibility_of(self.driver.find_element(By.TAG_NAME, "html")))
                    print(i+1,"ая вкладка открыта")
                    self.driver.close()
            self.driver.switch_to.window(original_window)
            i = i + 1



