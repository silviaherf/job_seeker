from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='./.env')




def jobs_scrapping():

    CHROME_PATH = os.getenv("CHROME_PATH")
    driver = webdriver.Chrome(CHROME_PATH)
    driver.get('https://www.linkedin.com/login/es?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    time.sleep(2)
    #assert "Linkedin" in driver.title
    
    username = driver.find_element_by_name('session_key')
    password = driver.find_element_by_name('session_password')
    
    username.send_keys(os.getenv("linkedin_user"))
    password.send_keys(os.getenv('linkedin_password'))
    time.sleep(0.3)
    button=driver.find_element(By.XPATH,'//*[@id="app__container"]/main/div[3]/form/div[3]/button')
    time.sleep(0.3)
    button.click()
    time.sleep(0.3)


    jobs=driver.find_element(By.XPATH,'//*[@id="ember26"]')
    time.sleep(0.3)
    jobs.click()
    time.sleep(0.3)

    
    #driver.close()

   