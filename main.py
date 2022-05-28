import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from input_test_data import *

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://localhost:1667/#/")
browser.maximize_window()


# browser.quit()

def sign_in():
    home_sign_in_btn = browser.find_elements_by_xpath('//a[@href="#/login"]')[0]
    # sign_in_btn = browser.find_elements_by_xpath('//a[normalize-space()="Sign in"]')[0]
    home_sign_in_btn.click()
    email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    email_input.send_keys(user1["email"])
    password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    password_input.send_keys(user1["password"])
    sign_in_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_btn.click()
    time.sleep(2)
    user_profile = browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
    # user_profile = browser.find_element_by_xpath('//a[@class="nav-link"][normalize-space()="szgteszt1"]')
    assert user_profile.text == user1["name"]  # helyes felhasználónév megjelenítésének ellenőrzése


def logout():
    logout_btn = browser.find_element_by_xpath('//a[@active-class="active"]')
    logout_btn.click()
    home_sign_in_btn = browser.find_elements_by_xpath('//a[@href="#/login"]')[0]
    assert home_sign_in_btn.text == "Sign in"


sign_in()
time.sleep(1)
logout()
