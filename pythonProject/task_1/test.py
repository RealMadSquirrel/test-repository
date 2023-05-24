import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


print("Выполнить один раз перед выполнением всех тестов")

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)
s = Service('C:/Users/user/PycharmProjects/pythonFirst/chromedriver.exe')
driver.implicitly_wait(10)
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.gloria-jeans.ru/")
time.sleep(6)
print('Все тесты пройдены')
driver.quit()


if __name__ == '__main__':
    unittest.main()