from itertools import product
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("http://orteil.dashnet.org/cookieclicker/")

time.sleep(3)

accept = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
accept.click()

lang = driver.find_element(By.ID, "langSelect-PL")
lang.click()

time.sleep(5)

cookie = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[15]/div[8]/button')
products = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[19]/div[3]/div[6]/*')
products.reverse()

def buyNewItems():
    buyMore = False
    for item in products:
        if item.get_attribute('class') == "product unlocked enabled":
            item.click()
            buyMore = True
            break
        
    if buyMore is True:
        buyNewItems()
            
clickCounter = 0 

while True:
    cookie.click()
    clickCounter += 1
    if clickCounter == 200:
        buyNewItems()
    
        clickCounter = 0
