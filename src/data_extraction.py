from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def jobs_scrapping(url='http://www.google.com/'):


    driver = webdriver.Chrome()
    driver.get('http://www.google.es/')
    time.sleep(5)
    assert "Google" in driver.title
    elem = driver.find_element_by_name("B")
    elem.send_keys(Keys.RETURN)
    driver.close()