import pytest
from selenium.webdriver.common.by import By
import time
import math

@pytest.mark.parametrize('path', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_site_authorization(browser, path):
    link = f"https://stepik.org/lesson/{path}/step/1"
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.ID, "id_login_email").send_keys("asdf@mail.ru")
    browser.find_element(By.ID, "id_login_password").send_keys("qwerty!")
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "[class='again-btn white']").click()
    time.sleep(5)
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, "[class='ember-text-area ember-view textarea string-quiz__textarea']").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "[class='submit-submission']").click()
    time.sleep(5)
    message = browser.find_element(By.CSS_SELECTOR, "[class='smart-hints__hint']").text
    assert "Correct!" in message, f"NOT CORRECT! actual result {message}"
