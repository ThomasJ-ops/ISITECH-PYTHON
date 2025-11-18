"""
Exercice 3 : Vérification de mot de passe
 Créez une fonction est_mot_de_passe_valide qui :
 Prend un mot de passe en paramètre
 Retourne True si le mot de passe :
    Fait au moins 8 caractères
    Contient au moins un chiffre
    Contient au moins une lettre majuscule
 Retourne False sinon
"""

# Fonction de vérification
def est_mot_de_passe_valide(mdp):
    """
    Vérifie si le mot de passe est valide.
        args:
            mdp (str): Le mot de passe à vérifier.
        returns:
            bool: True si le mot de passe est valide, False sinon.
    """

    """
    ## Vérification Longueur
    if len(mdp) < 8:
        return False
    
    ## Vérification s'il y à au moins un Chiffre

    contient_chiffre = False
    for character in mdp:
        if character.isdigit():
            contient_chiffre = True
            break

    ## Vérification Majuscule

    contient_majuscule = False
    for character in mdp:
        if character.isupper():
            contient_majuscule = True
            break

    return contient_chiffre and contient_majuscule
"""
def est_mot_de_passe_valide(mdp):
    longueur_ok = len(mdp) >= 8
    contient_chiffre = any(c.isdigit() for c in mdp)
    contient_majuscule = any(c.isupper() for c in mdp)

    return longueur_ok and contient_chiffre and contient_majuscule



# Utilisation
Mot_De_Passe = "Test123456"
Verificatoin_MDP = est_mot_de_passe_valide(Mot_De_Passe)

print(f" Le mot de passe {Mot_De_Passe} est valide: {Verificatoin_MDP}")
