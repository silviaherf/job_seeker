from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='src/.env')



def jobs_scrapping(username, password):

    CHROME_PATH = os.getenv("CHROME_PATH")
    driver = webdriver.Chrome(CHROME_PATH)
    driver.get('https://www.linkedin.com/login/es?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    time.sleep(5)
    assert "Linkedin" in driver.title
    username = driver.find_element_by_name('session_key')
    password = driver.find_element_by_name('session_password')
    username = os.getenv("linkedin_user")
    password = os.getenv('linkedin_password')

    elem = driver.find_element_by_name("B")
    



    driver.close()