from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner

class search(unittest.TestCase):
    def google(driver):
        driver = webdriver.Chrome("./chromedriver.exe")
        driver.get("https://www.google.com")

    def apacheJmeter(driver):
        accept = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div")
        accept.click()

        search = driver.find_element(By.NAME, "q")
        search.send_keys("Apache Jmeter")
        search.send_keys(Keys.RETURN)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/kacpe/OneDrive/Pulpit/Tests/Selenium"))
