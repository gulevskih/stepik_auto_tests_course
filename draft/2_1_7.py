from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.ID, 'treasure').get_attribute("valuex")
result = str(log(abs(12*sin(int(x)))))
print(result)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(result)

checkbox = browser.find_element(By.ID, 'robotCheckbox')
checkbox.click()

radiobutton = browser.find_element(By.ID, 'robotsRule')
radiobutton.click()

button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button.click()

time.sleep(30)
browser.quit()
