from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "','usr','local','bin','chromedriver"
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.by import By

def launchBrowser(nb):
   print("chargement de la liste de mots...")
   match nb:
         case 100:
            liste = open("words/liste100.txt", "r")
         case 1000:
            liste = open("words/liste1000.txt", "r")
         case 10000:
            liste = open("words/liste10000.txt", "r")
         case 600000:
            liste = open("words/liste600000.txt", "r")
         case _ :
            liste = open("words/liste_opti.txt", "r")

   print("liste chargée !")
   print("on a chargé la liste de "+str(nb)+" mots")
   words = liste.read().split(',')
   driver.get("https://cemantix.certitudes.org/pedantix")
   print(driver.title)
   for word in words:
       search = driver.find_element(By.ID, "pedantix-guess")
       search.send_keys(word)
       search.send_keys(Keys.RETURN)
       time.sleep(0.1)  
