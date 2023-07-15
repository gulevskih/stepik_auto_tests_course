from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.ID, "input_value").text
result = str(log(abs(12*sin(int(x)))))

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(result)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(30)
browser.quit()
