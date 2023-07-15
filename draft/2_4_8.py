from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import *
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока значение кпопки не станет $100
# сразу после этого переходит к следующему шагу, где кликает на нужную кнопку
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
browser.find_element(By.ID, "book").click()

x = browser.find_element(By.ID, "input_value").text
result = str(log(abs(12*sin(int(x)))))

form = browser.find_element(By.ID, "answer")
form.send_keys(result)

button = browser.find_element(By.ID, "solve").click()

time.sleep(30)
browser.quit()

