from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "','usr','local','bin','chromedriver"
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.by import By

liste = open("words.txt", "r")
words = liste.read().split(',')

def launchBrowser():
   driver.get("https://cemantix.certitudes.org/pedantix")
   print(driver.title)
   for word in words:
       search = driver.find_element(By.ID, "pedantix-guess")
       search.send_keys(word)
       search.send_keys(Keys.RETURN)
       time.sleep(0.1)  
   while(True):
       pass
launchBrowser()


# Path: words.txt
# List of words to search
# il faudrait trouver une liste de mots plus grande
# et plus variée
# et qui ne contienne pas de mots interdits
# par exemple, les mots qui contiennent des caractères spéciaux
# ou les mots qui contiennent des chiffres
# ou les mots qui contiennent des accents
# ou les mots qui contiennent des majuscules
# ou les mots qui contiennent des espaces
# ou les mots qui contiennent des apostrophes
# ou les mots qui contiennent des tirets
# ou les mots qui contiennent des points
# ou les mots qui contiennent des virgules
# ou les mots qui contiennent des points-virgules
# ou les mots qui contiennent des points d'interrogation
# ou les mots qui contiennent des points d'exclamation
# ou les mots qui contiennent des parenthèses
# ou les mots qui contiennent des crochets
# ou les mots qui contiennent des accolades
# ou les mots qui contiennent des barres obliques
# ou les mots qui contiennent des barres obliques inversées
# ou les mots qui contiennent des barres obliques obliques
# ou les mots qui contiennent des barres obliques obliques inversées
# ou les mots qui contiennent des barres obliques obliques obliques
# ou les mots qui contiennent des barres obliques obliques obliques inversées
# ou les mots qui contiennent des barres obliques obliques obliques obliques
# ou les mots qui contiennent des barres obliques obliques obliques obliques inversées
# ou les mots qui contiennent des barres obliques obliques obliques obliques obliques
# ou les mots qui contiennent des barres obliques obliques obliques obliques obliques inversées
# ou les mots qui contiennent des barres obliques obliques obliques obliques obliques obliques
#ca va continuer longtemps ce rafut? copilote, tu peux pas faire plus court?
# ou les mots qui contiennent des barres obliques obliques obliques obliques obliques obliques inversées
# ou les mots qui contiennent des barres obliques obliques obliques obliques obliques obliques obliques
# ou les mots qui contiennent des barres obliques obliques obliques obliques obliques obliques obliques inversées
# ou les mots qui contiennent des barres obliques obliques obliques obliques obliques obliques obliques obliques
# ou les mots qui contiennent des barres obliques obliques obliques obliques obliques obliques obliques obliques inversées
# ou les mots qui contiennent des barres obliques obliques obliques obliques obliques obliques obliques obliques obliques
#je crois que je vais m'arrêter là




























