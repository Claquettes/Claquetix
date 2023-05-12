from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "','usr','local','bin','chromedriver"
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.by import By

def launchBrowser(nb):
   global liste
   if nb == 10000:
       liste = open("10k.txt", "r")
   else :
         liste = open("words.txt", "r")

    
   words = liste.read().split(',')
   driver.get("https://cemantix.certitudes.org/pedantix")
   print(driver.title)
   for word in words:
       search = driver.find_element(By.ID, "pedantix-guess")
       search.send_keys(word)
       search.send_keys(Keys.RETURN)
       time.sleep(0.1)  
   while(True):
       pass
