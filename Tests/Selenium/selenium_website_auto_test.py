from ast import Return
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("https://mediamarkt.pl/")

