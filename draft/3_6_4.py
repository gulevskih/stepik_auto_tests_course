from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/236895/step/1"

def test_site_authorization(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.ID, "id_login_email").send_keys("asdf@mail.ru")
    browser.find_element(By.ID, "id_login_password").send_keys("qwerty!")
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(10)
