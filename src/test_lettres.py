fichier_mot = open("words/liste_opti.txt", "r")
liste_mots = fichier_mot.read().split(',')
fichier_mot.close()

nombre=0
for mots in liste_mots:
    vrai_mot=""
    change=0
    for lettre in mots:
        if (lettre=='\n'):#on passe à la ligne suivante
            continue
        elif (lettre=='©') :
            vrai_mot = vrai_mot[:-1] + 'é'
        elif (lettre=='¨') :
            vrai_mot = vrai_mot[:-1] + 'è'
        elif (lettre=='Ã'):
            change=1
            vrai_mot+="à"
        elif (lettre=='¢'):
            vrai_mot = vrai_mot[:-1] + 'â'
        elif (lettre=='ª'):
            vrai_mot = vrai_mot[:-1] + 'ê'
        elif (lettre=='®'):
            vrai_mot = vrai_mot[:-1] + 'î'
        elif (lettre=='¹'):
            vrai_mot = vrai_mot[:-1] + 'ù'
        elif (lettre=='´'):
            vrai_mot = vrai_mot[:-1] + 'ô'
        elif (lettre=='§'):
            vrai_mot = vrai_mot[:-1] + 'ç'
        elif (lettre=='¯'):
            vrai_mot = vrai_mot[:-1] + 'ï'
        elif (lettre=='»'):
            vrai_mot = vrai_mot[:-1] + 'û'
        else : vrai_mot+=lettre
    lettre_prec=lettre
    
    #on remplace dans la liste le mot mal écrit par le mot bien écrit
    if (change ==1) : print(vrai_mot)
    nombre+=1