from ast import Return
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Booking(webdriver.Chrome):
    def __init__(driver):
        driverPath = "./chromedriver.exe"
        driverPath()
        super(Booking, driver).__init__()
        
        
    def CloseMap(driver):
        driver.get("https://www.youtube.com") 