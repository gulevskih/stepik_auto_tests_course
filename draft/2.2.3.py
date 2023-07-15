from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, 'num1').text
num2 = browser.find_element(By.ID, 'num2').text
result = int(num1) + int(num2)

Select(browser.find_element(By.ID, 'dropdown')).select_by_value(str(result))

button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button.click()

time.sleep(30)
browser.quit()
