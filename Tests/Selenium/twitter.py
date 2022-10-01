from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def importHastag(hash):
    pattern = "#(\w+)"
    return re.findall(pattern, hash)

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://twitter.com/search?q=python&src=typed_query")

postsLoaded = EC.presence_of_element_located((By.TAG_NAME, 'article'))
WebDriverWait(driver, 15).until(postsLoaded)

for post in driver.find_elements(By.TAG_NAME, 'article'):
    try:
        print(importHastag(post.find_element(By.CSS_SELECTOR, '[lang="pl"]').text))
    except NoSuchElementException:
        continue