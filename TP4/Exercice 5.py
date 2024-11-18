myDictionnaire = {'nom':"Dupont",'prenom':"Maurice",'age':90,'sal':59000}
print(myDictionnaire)
inv_dictionnaire = { valeur:cle for cle,valeur in myDictionnaire.items()}
print(inv_dictionnaire)