"""
 Exercices pratiques
 Exercice 1 : Fonction de salutation
 Créez une fonction 
saluer_personne
 qui :
 Prend en paramètre un nom et une heure (0-23)
 Retourne "Bonjour" si l'heure est entre 6 et 12
 Retourne "Bon après-midi" si l'heure est entre 12 et 18
 Retourne "Bonsoir" si l'heure est entre 18 et 24
 Retourne "Bonne nuit" pour les autres heures

"""



def Saluer_personne(Nom, heure):
    """
    Retourne une réponse en fonction du prénom et de l'heure indiquée
    """
    heure = int(heure)

    if  6 <= heure < 12:
        message = "Bonjour"
    elif 12 <= heure < 18:
        message = "Bon après-midi"
    elif 18 <= heure < 24:
        message = "Bonsoir"
    else: 
        message = "Bonne nuit"
    # return(f" {message}, {Nom}, !")

# utilisation
personne1 = Saluer_personne("Alice", "20")
personne2 = Saluer_personne("Bob", "10")
personne3 = Saluer_personne("Charlie", "14")

# Exemple d'utilisation
print(f"{personne1} ")





    