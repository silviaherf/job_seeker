from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='./.env')




def jobs_scrapping(key='data',city='Madrid'):

    CHROME_PATH = os.getenv("CHROME_PATH")
    driver = webdriver.Chrome(CHROME_PATH)
    driver.get('https://www.linkedin.com/login/es?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    time.sleep(2)
 
    
    username = driver.find_element_by_name('session_key')
    password = driver.find_element_by_name('session_password')
    
    username.send_keys(os.getenv("linkedin_user"))
    password.send_keys(os.getenv('linkedin_password'))
    time.sleep(0.3)
    button=driver.find_element(By.XPATH,'//*[@id="app__container"]/main/div[3]/form/div[3]/button')
    time.sleep(0.5)
    button.click()
    time.sleep(1)


    jobs=driver.find_element(By.XPATH,'//*[@id="ember26"]')
    time.sleep(0.3)
    jobs.click()
    time.sleep(0.3)

    #key=driver.find_element_by_class_name('jobs-search-box__text-input')
    #key=driver.find_element_by_css_selector('input.jobs-search-box-keyword-id-ember644')
    key=driver.find_element_by_css_selector(".jobs-search-box__text-input jobs-search-box__ghost-text-input[aria-label='Busca por cargo, aptitud o empresa']")
    key.send_keys(key)
    time.sleep(0.3)
    city=driver.find_element(By.XPATH,'//*[@id="jobs-search-box-location-id-ember621"]')
    city.send_keys(city)
    time.sleep(0.3)
    find=driver.find_element(By.CLASS_NAME,'jobs-search-box__submit-button artdeco-button artdeco-button--3 jobs-home-soho__mvp-button')
    time.sleep(0.3)
    find.click()

    
    #driver.close()

   