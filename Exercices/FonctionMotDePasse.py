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
    """
    if len(mdp) < 8:
        return False

    contient_chiffre = False
    for character in mdp:
        if character.isdigit():
            contient_chiffre = True
            break

    contient_majuscule = False
    for character in mdp:
        if character.isupper():
            contient_majuscule = True
            break

    return contient_chiffre and contient_majuscule


# Utilisation
Mot_De_Passe = "Test123456"
Verificatoin_MDP = est_mot_de_passe_valide(Mot_De_Passe)

print(f" Le mot de passe {Mot_De_Passe} est valide: {Verificatoin_MDP}")
