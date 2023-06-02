import unittest
import time
from selenium import webdriver


print("Выполнить один раз перед выполнением всех тестов")

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.gloria-jeans.ru/")
time.sleep(6)
print('Все тесты пройдены')
driver.quit()


if __name__ == '__main__':
    unittest.main()