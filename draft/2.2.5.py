from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = int(browser.find_element(By.ID, "input_value").text)
result = str(log(abs(12*sin(x))))

footer = browser.find_element(By.TAG_NAME, "footer")
browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(result)

checkbox = browser.find_element(By.ID, 'robotCheckbox')
checkbox.click()

radiobutton = browser.find_element(By.ID, 'robotsRule')
radiobutton.click()


button = browser.find_element(By.TAG_NAME, "button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(30)
browser.quit()
