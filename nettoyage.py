fichier_mots = open("ref_text/french01.txt", "r")
liste_mots = fichier_mots.read().split(',')
#l'objectif est de supprimer tout les doublons
#et de supprimer les mots qui ne sont pas des mots
#de la langue française depuis words.txt
fichier_mots.close()
fichier_mots = open("french1K.txt", "r")

for mot2 in fichier_mots.read().split(','):
    if mot2 not in liste_mots:
        liste_mots.append(mot2)




#on écrit dans words2.txt tout les mots avec ceux les plus courrants en premier
fichier_rslt = open("words2.txt", "w")
