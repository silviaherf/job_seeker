from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='./.env')
from pyvirtualdisplay import Display




def jobs_scrapping(key='data',city='Madrid'):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    CHROME_PATH = os.getenv("CHROME_PATH")
    driver = webdriver.Chrome(CHROME_PATH, chrome_options=chrome_options)
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
    time.sleep(0.5)


    jobs = driver.find_element_by_link_text('Empleos')
    time.sleep(0.3)
    jobs.click()
    time.sleep(0.3)

   
    
    
    key_find=driver.find_element_by_xpath("//*[@class='ember-view']/input[1]")
    key_find.clear()
    key_find.send_keys(key)
    time.sleep(0.3)


#Pendiente revisar city
    city=driver.find_element_by_xpath("//*[contains(@id,'jobs-search-box-location-id-ember')]")
    city.clear()
    city.send_keys(city)

    time.sleep(0.3)
    find=driver.find_element(By.CLASS_NAME,'jobs-search-box__submit-button artdeco-button artdeco-button--3 jobs-home-soho__mvp-button')
    time.sleep(0.3)
    find.click()



    
    #driver.close()

   