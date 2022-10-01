from ast import Return
from atexit import register
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("./chromedriver.exe")

path = driver.get("https://www.booking.com")
driver.fullscreen_window
        
currency = driver.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Wybierz walutę"]')
currency.click()
        
accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
accept.click()
        
choosecurrency = driver.find_element(By.CSS_SELECTOR, 'a[data-modal-header-async-url-param*="selected_currency=EUR"]')
choosecurrency.click()

search = driver.find_element(By.ID, "ss")
search.send_keys("Kraków")
search.send_keys(Keys.RETURN)
        
changeLanguage = driver.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Wybierz język"]')
changeLanguage.click()
        
chooseLanguage = driver.find_element(By.CSS_SELECTOR, 'a[data-lang="en-gb"]')
chooseLanguage.click()
        
chooseStartDay = driver.find_element(By.CSS_SELECTOR, 'span[data-date="2022-09-11"]')
chooseStartDay.click()
        
changeLanguageAgain = driver.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your language"]')
changeLanguageAgain.click()

chooseLanguagePolish = driver.find_element(By.CSS_SELECTOR, 'a[data-lang="pl"]')
chooseLanguagePolish.click()
        
chooseStartDayinPolish = driver.find_element(By.CSS_SELECTOR, 'span[data-date="2022-09-11"]')
chooseStartDayinPolish.click()
        
chooseEndDate = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="date-display-field-end"]')
chooseEndDate.click()
        
chooseEndDay = driver.find_element(By.CSS_SELECTOR, 'span[data-date="2022-09-15"]')
chooseEndDay.click()
        
searchApartaments = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
searchApartaments.click()
  
openMap = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="map-trigger"]')
openMap.click()

closingMapObject = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Close map"]')
closingMapObject.click() 

applyStarsOfApartaments = driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
starFiltrations = applyStarsOfApartaments.find_elements(By.CSS_SELECTOR, '*')

for starElement in starFiltrations:
    if str(starElement.get_attribute('innerHTML')).strip() == '4 gwiazdki':
        starElement.click()
        
        
applyPrice = driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="pri"]')
priceFiltration = applyPrice.find_elements(By.CSS_SELECTOR, '*')

for priceElement in priceFiltration:
    if str(priceElement.get_attribute('innerHTML')).strip() == '€&nbsp;150–€&nbsp;200':
        priceElement.click()
    
   
registerToPortal = driver.find_element(By.CSS_SELECTOR, 'a[data-google-track="Click/Action: searchresults/header_logged_out_link_box"]')
registerToPortal.click()

appendEmail = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
appendEmail.send_keys("kacpersalamon1707@gmail.com")
appendEmail.send_keys(Keys.RETURN)

backToLogin = driver.find_element(By.CSS_SELECTOR, 'button[type="button"]')
backToLogin.click()

loginByGoogle = driver.find_element(By.CSS_SELECTOR, 'a[data-provider-name="google"]')
loginByGoogle.click()
driver.get_log()

 
#clikcApartaments = driver.find_element(By.LINK_TEXT, "Xerion Hotel").find_element(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
#clikcApartaments.click()



    
            


