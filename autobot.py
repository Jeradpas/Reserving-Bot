# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:18:25 2020

@author: adrie
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import send_sms as message


PATH = "C:\Program Files (x86)\chromedriver.exe"
URL = 'https://www.envoituresimone.com/'

driver = webdriver.Chrome(PATH)
driver.get(URL)
print(driver.title)

driver.find_element_by_id('accept_cookies').send_keys(Keys.RETURN)
driver.find_element_by_link_text('Se connecter').send_keys(Keys.RETURN)

try:
    print("Looking for the FB button")
    main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"facebook-connect")))
    driver.find_element_by_partial_link_text('Facebook').click()
    print("Fb found")
    
except:
    print("Fb not found")
    driver.quit()

#Connection à Facebook
try:
    main = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.ID,"u_0_g")))
    main.click()
except:
    driver.quit()
    
driver.find_element_by_id("u_0_g").send_keys(Keys.RETURN)
driver.find_element_by_id('email').send_keys("******************")
driver.find_element_by_id('pass').send_keys("************************")
driver.find_element_by_id('loginbutton').send_keys(Keys.RETURN)
print("Connecté à Facebook")

#Bouton reserver une lecon
try:
    main=WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.XPATH,"/html/body/app-root/ion-app/ion-router-outlet/dashboard-page/ion-content/div[2]/div/div/div[2]/stats-calendar/button")))
    main.click()
except:
    driver.quit()
    
#Bouton par adresse
try:
    
    main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"adresse")))
    driver.find_element_by_partial_link_text('adresse').click()
except:
    driver.quit()
    

try:    
    main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"new_lesson_address_input")))
    main.send_keys("3 Place Saint-Nizier, Lyon")
    time.sleep(1)
    print("load possibilities")
    main.send_keys(Keys.RETURN)
except:
    print("Not found")
    driver.quit()
time.sleep(5)
possibilities = driver.find_elements_by_tag_name("a")
for p in possibilities:
    print(p.text)
driver.find_element_by_partial_link_text('Prochain').click()
message.send('Reservation disponible')

