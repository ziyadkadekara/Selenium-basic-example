from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time  
print("sample test case started")  
driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get("https://www.google.com/")  
elem = driver.find_element(By.NAME, 'q')
elem.send_keys('Object Oriented Software Engineering')
time.sleep(3)  
elem.send_keys(Keys.ENTER)
time.sleep(3)  
driver.close()  
print("sample test case successfully completed")  