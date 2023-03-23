from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


x = browser.find_element(By.ID, "input_value").text
result = str(log(abs(12*sin(int(x)))))

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(result)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(30)
browser.quit()
