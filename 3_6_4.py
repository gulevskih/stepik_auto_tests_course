import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="session")
def app():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield app
    print("\nquit browser..")
    browser.quit()

link = "https://stepik.org/lesson/236895/step/1"

def test_site_authorization(app):
    browser.get(link)
    browser.find_element(By.ID, "ember33")
    browser.find_element(By.ID, "id_login_email").send_keys("123")
    browser.find_element(By.ID, "id_login_password").send_keys("456")
    browser.find_element(By.TAG_NAME, "button")
    time.sleep(30)
