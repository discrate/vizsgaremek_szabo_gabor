import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from input_test_data import *

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://localhost:1667/#/")
browser.maximize_window()

# browser.quit()

# Teszteset 01 -- Regisztráció helytelen adatokkal
# def registration_invalid():
#     sign_up_btn = browser.find_element_by_xpath('//a[@href="#/register"]')
#     sign_up_btn.click()
#     username_input = browser.find_element_by_xpath('//input[@placeholder="Username"]')
#     email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
#     password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
#     sign_up_send_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
#     username_input.send_keys(user3["name"])
#     email_input.send_keys("incorrect")
#     password_input.send_keys(user3["password"])
#     sign_up_send_btn.click()
#     time.sleep(2)
#     result_message = browser.find_element_by_xpath('//div[@class="swal-title"]')
#     result_reason = browser.find_element_by_xpath('//div[@class="swal-text"]')
#     try:
#         assert result_message.text == "Registration failed!"
#         assert result_reason.text == "Email must be a valid email."
#         print('Helyes hibaüzenet')
#     except AssertionError:
#         print('Helytelen validáció')


# Teszteset 02 -- Regisztráció helyes adatokkal
# def registration_valid():
#     sign_up_btn = browser.find_element_by_xpath('//a[@href="#/register"]')
#     sign_up_btn.click()
#     username_input = browser.find_element_by_xpath('//input[@placeholder="Username"]')
#     email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
#     password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
#     sign_up_send_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
#     username_input.send_keys("szgteszt998")
#     email_input.send_keys("szgteszt998@gmail.com")
#     password_input.send_keys(user3["password"])
#     sign_up_send_btn.click()
#     time.sleep(2)
#     result_message = browser.find_element_by_xpath('//div[@class="swal-title"]')
#     result_reason = browser.find_element_by_xpath('//div[@class="swal-text"]')
#     try:
#         assert result_message.text == "Welcome!"
#         assert result_reason.text == "Your registration was successful!"
#         print('Sikeres regisztráció')
#     except AssertionError:
#         print('Sikertelen regisztráció')
#
#     ok_btn = browser.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
#     ok_btn.click()


# Teszteset 03 -- Bejelentkezés
# def sign_in():
#     home_sign_in_btn = browser.find_elements_by_xpath('//a[@href="#/login"]')[0]
#     # sign_in_btn = browser.find_elements_by_xpath('//a[normalize-space()="Sign in"]')[0]
#     home_sign_in_btn.click()
#     email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
#     email_input.send_keys(user1["email"])
#     password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
#     password_input.send_keys(user1["password"])
#     sign_in_btn = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
#     sign_in_btn.click()
#     time.sleep(2)
#     user_profile = browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
#     # user_profile = browser.find_element_by_xpath('//a[@class="nav-link"][normalize-space()="szgteszt1"]')
#     try:
#         assert user_profile.text == user1["name"]  # helyes felhasználónév megjelenítésének ellenőrzése
#         print('Sikeres bejelentkezés')
#     except AssertionError:
#         print('Nem sikerült bejelentkezni')


# Teszteset 04 -- Adatkezelési nyilatkozat használata
# def accept_cookies():
#     accept_btn = browser.find_element_by_xpath('//div[normalize-space()="I accept!"]')
#     accept_btn.click()
#     time.sleep(1)
#     decline_btn_list = browser.find_elements_by_xpath('//div[normalize-space()="I decline!"]')
#     print(len(decline_btn_list))
#     assert len(decline_btn_list) == 0


# Teszteset 12 -- Kijelentkezés       # már bejelentkezett a user és elég csak logoutolni vagy login-t is meg kell hívni előtte???
# def logout():
#     logout_btn = browser.find_element_by_xpath('//a[@active-class="active"]')
#     logout_btn.click()
#     home_sign_in_btn = browser.find_elements_by_xpath('//a[@href="#/login"]')[0]
#     try:
#         assert home_sign_in_btn.text == "Sign in"
#         print('Sikeres kijelentkezés')
#     except AssertionError:
#         print('Nem sikerült kijelentkezni')
