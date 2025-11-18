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


def saluer_personne(nom, heure):
    """
    Retourne le message de salutation en fonction de l'heure.

    paramètre:
        nom (str): Le nom de la personne.
        heure (int): L'heure de la journée (0-23)
    """
    
    heure = int(heure)
    
    if heure > 23 or heure < 0:
        return "l'heure doit être comprise entre 0 et 23"
    
    ##try:


    

    if 6 <= heure < 12:
        return "Bonjour"
    elif 12 <= heure < 18:
        return "Bon après-midi"
    elif 18 <= heure <= 23:
        return "Bonsoir"
    else:
        return "Bonne nuit"

nom_a = "Alice"
nom_b = "Bob"
nom_c = "Luc"

print(saluer_personne("Alice", "10")+ " " + nom_a)
print(saluer_personne("Bob", "22")+ " " + nom_b)
print(saluer_personne("Luc", "16")+ " " + nom_c)

    