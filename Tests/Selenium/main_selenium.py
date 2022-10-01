from ast import Return
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("https://mediamarkt.pl/")
driver.fullscreen_window

#left_bar = driver.find_element(By.LINK_TEXT, "Telefony i Smartwatche")
#left_bar.click()

#box = driver.find_element(By.CLASS_NAME, "input-inner")
#box.send_keys("iphone 11")
#box.send_keys(Keys.RETURN)

login = driver.find_element(By.LINK_TEXT, "Zaloguj się")
login.click()

email = driver.find_element(By.ID, "enp_customer_form_login_username")
email.send_keys("kacpersalamon1707@gmail.com")

password = driver.find_element(By.ID, "enp_customer_form_login_password")
password.send_keys("Iza070118")

login_2 = driver.find_element(By.LINK_TEXT, "Zaloguj się")
login_2.click()




