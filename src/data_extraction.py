from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import os
from bson.json_util import dumps
from dotenv import load_dotenv
load_dotenv(dotenv_path='./.env')
from pyvirtualdisplay import Display


class Linkedin:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--window-size=1420,1080')
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--disable-gpu')

        #We open a webbrowser in Google Chrome
        CHROME_PATH = os.getenv("CHROME_PATH")
        self.driver = webdriver.Chrome(CHROME_PATH, chrome_options=chrome_options)
        self.driver.get('https://www.linkedin.com/login/es?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        time.sleep(2)


    def jobs(self,key='data',city='Madrid'):
        #We login

        username = self.driver.find_element_by_name('session_key')
        password = self.driver.find_element_by_name('session_password')
        
        username.send_keys(os.getenv("linkedin_user"))
        password.send_keys(os.getenv('linkedin_password'))
        time.sleep(0.3)
        button=self.driver.find_element(By.XPATH,'//*[@id="app__container"]/main/div[3]/form/div[3]/button')
        
        time.sleep(0.5)
        button.click()
        time.sleep(0.5)

        #We change to the jobs page
        jobs = self.driver.find_element_by_link_text('Empleos')
        time.sleep(0.3)
        jobs.click()
        time.sleep(0.3)

    
        #We enter our keywords for job seeking: job type and location
        key_find = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='ember-view'][@aria-label='Busca por cargo, aptitud o empresa']/input[1]"))
        )
            
        
        key_find.clear()
        time.sleep(0.3)
        key_find.send_keys(key)
        time.sleep(0.3)


        key_city=self.driver.find_element_by_xpath("//*[@class='ember-view'][@aria-label='Ciudad, provincia o código postal']/input[1]")
        key_city.clear()
        key_city.send_keys(city)
        key_city.send_keys('\n')
        time.sleep(0.3)

    def filters(self):
        #We filter for the latest jobs
        find = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Filtro «Fecha de publicación». Al hacer clic en este botón, se muestran todas las opciones del filtro «Fecha de publicación».']"))
        )
        
        time.sleep(0.3)
        
        find.click()
      
        
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(self.driver.find_element(By.XPATH, "//input[@name='Últimas 24 horas']"), 5,5).click().perform()
        time.sleep(0.3)

        #We filter for jobs with the the easy application option 
        funcionalities=self.driver.find_element(By.XPATH, "//button[@aria-label='Todos los filtros']")
        funcionalities.click()

        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(self.driver.find_element(By.XPATH, "//input[@name='Solicitud sencilla']"), 5,7).click().perform()


    def more_jobs(self):
        #We look up through every page of results
        numero=self.driver.find_element_by_xpath("//ul/li[last()]/button[1]").get_attribute("aria-label")
        n=int(re.findall(r'\d+',numero)[0])
        for i in range (1,n-1):
            self.driver.find_element(By.XPATH, f"//button[@aria-label=f'Página {i+1}']").click()


    def apply(self):
        pass
        #self.driver.close()
        
        

    
   