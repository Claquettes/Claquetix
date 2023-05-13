fichier_mots = open("ref_text/french01.txt", "r")
liste_mots = fichier_mots.read().split(',')
#l'objectif est de supprimer tout les doublons
#et de supprimer les mots qui ne sont pas des mots
#de la langue française depuis words.txt
fichier_mots.close()
fichier_mots = open("ref_text/french1K.txt", "r")
for mot2 in fichier_mots.read().split(','):
    ok=True
    for mot_pris in liste_mots:
        if mot2 == mot_pris:
            ok=False
    if (ok) : liste_mots.append(mot2)

fichier_mots.close()
fichier_mots = open("ref_text/french2K.txt", "r")
for mot2 in fichier_mots.read().split(','):
        ok=True
        for mot_pris in liste_mots:
            if mot2 == mot_pris:
                ok=False
        if (ok) : liste_mots.append(mot2)
fichier_mots.close()
fichier_mots = open("ref_text/french10K.txt", "r")
for mot2 in fichier_mots.read().split(','):
        ok=True
        for mot_pris in liste_mots:
            if mot2 == mot_pris:
                ok=False
        if (ok) : liste_mots.append(mot2)
fichier_mots.close()

#on écrit dans words2.txt tout les mots avec ceux les plus courrants en premier
fichier_rslt = open("ref_text/words2test.txt", "w")
for mot in liste_mots:
    fichier_rslt.write(mot + ",")
fichier_rslt.close()