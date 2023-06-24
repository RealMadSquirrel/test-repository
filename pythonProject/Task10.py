import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

class test_10(unittest.TestCase):
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

    def test_1_title(self):
        box = self.driver.find_element(By.XPATH, "//*[@id='box-campaigns']")
        product = box.find_element(By.CLASS_NAME, "name")
        h_1 = product.text

        box.find_element(By.CLASS_NAME, "link").click()
        title = self.driver.find_element(By.TAG_NAME, "h1")
        h_2 = title.text
        if h_1 == h_2:
            print("Тест пройден", h_1, "=", h_2)
        self.driver.back()


    def test_2_price(self):
        box = self.driver.find_element(By.XPATH, "//*[@id='box-campaigns']")
        price1_1 = box.find_element(By.CLASS_NAME, "campaign-price")
        price1_2 = box.find_element(By.CLASS_NAME, "regular-price")
        p_1_1 = price1_1.text
        p_1_2 = price1_2.text
        box.find_element(By.CLASS_NAME, "link").click()
        price2_1 = self.driver.find_element(By.CLASS_NAME, "campaign-price")
        price2_2 = self.driver.find_element(By.CLASS_NAME, "regular-price")
        p_2_1 = price2_1.text
        p_2_2 = price2_2.text
        if p_1_1 == p_2_1 and p_1_2 == p_2_2:
            print("Тест пройден", p_1_1, "=", p_2_1,p_1_2, "=",p_2_2)
        else:
            print("Тест не пройден")
        self.driver.back()

    def test_3_price_color_grey(self):
        box = self.driver.find_element(By.XPATH, "//*[@id='box-campaigns']")
        price1 = box.find_element(By.CLASS_NAME, "regular-price")
        color_grey1 = re.findall(r"\d+", price1.value_of_css_property("color"))
        text_decoration1 = price1.value_of_css_property("text-decoration").split()
        box.find_element(By.CLASS_NAME, "link").click()
        price2 = self.driver.find_element(By.CLASS_NAME, "regular-price")
        color_grey2 = re.findall(r"\d+", price2.value_of_css_property("color"))
        text_decoration2 = price2.value_of_css_property("text-decoration").split()
        if int(color_grey1[0]) == int(color_grey1[1]) == int(color_grey1[2]) and int(color_grey2[0]) == int(
                color_grey2[1]) == int(color_grey2[2]) and text_decoration1[0] == "line-through" and text_decoration2[
            0] == "line-through":
            print("Тест пройден", color_grey1[0], color_grey1[1], color_grey1[2], "и", color_grey2[0], color_grey2[1],
                  color_grey2[2], "- одинаковые значения для каналов R, G и B и обычная цена зачёркнутая")
        else:
            print("Тест не пройден")
        self.driver.back()

    def test_4_price_color_red(self):
        box = self.driver.find_element(By.XPATH, "//*[@id='box-campaigns']")
        price1 = box.find_element(By.CLASS_NAME, "campaign-price")
        color_grey1 = re.findall(r"\d+", price1.value_of_css_property("color"))
        font_weight1 = price1.value_of_css_property("font-weight")
        box.find_element(By.CLASS_NAME, "link").click()
        price2 = self.driver.find_element(By.CLASS_NAME, "campaign-price")
        color_grey2 = re.findall(r"\d+", price2.value_of_css_property("color"))
        font_weight2 = price2.value_of_css_property("font-weight")
        if int(color_grey1[1]) == 0 and int(color_grey1[2]) == 0 and int(color_grey2[1]) == 0 and int(
                color_grey2[2]) == 0 and int(font_weight1) >= 700 and int(font_weight2) >= 700:
            print("Тест пройден", color_grey1[1], color_grey1[2], "и", color_grey2[1], color_grey2[2],
                  "- каналы G и B имеют нулевые значения и акционная цена жирная")
        else:
            print("Тест не пройден")
        self.driver.back()


    def test_5_price_size(self):
        box = self.driver.find_element(By.XPATH, "//*[@id='box-campaigns']")
        font_size1 = box.find_element(By.CLASS_NAME, "campaign-price").value_of_css_property("font-size")
        font_size2 = box.find_element(By.CLASS_NAME, "regular-price").value_of_css_property("font-size")
        font_size1 = re.findall(r"\d+\.\d+|\d+", font_size1)
        font_size2 = re.findall(r"\d+\.\d+|\d+", font_size2)
        if float(font_size1[0]) > float(font_size2[0]):
            print("Тест пройден", font_size1[0], ">", font_size2[0])
        else:
            print("Тест не пройден")

        box.find_element(By.CLASS_NAME, "link").click()
        font_size3 = self.driver.find_element(By.CLASS_NAME, "campaign-price").value_of_css_property("font-size")
        font_size4 = self.driver.find_element(By.CLASS_NAME, "regular-price").value_of_css_property("font-size")
        font_size3 = re.findall(r"\d+\.\d+|\d+", font_size3)
        font_size4 = re.findall(r"\d+\.\d+|\d+", font_size4)
        if float(font_size3[0]) > float(font_size4[0]):
            print("Тест пройден", font_size3[0], ">", font_size4[0])
        else:
            print("Тест не пройден")
        self.driver.back()

if __name__ == '__main__':
    unittest.main()
