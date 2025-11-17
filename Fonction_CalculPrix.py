"""
 Exercice 2 : Calculatrice de prix

 Créez une fonction calculer_prix_ttc qui :
 Prend en paramètre un prix HT et un taux de TVA (par défaut 20%)
 Calcule et retourne le prix TTC
 Arrondit le résultat à 2 décimales
"""
#Définission Variable


## Fontion de calcul 

def Calculer_prix_ttc(HT, TVA):
    """
    Calcule le prix TTC à partir du prix HT et du taux de TVA.
    """
    TTC = HT * (1 + TVA / 100)
    return round(TTC, 2)

#utilisation 
prix_HT = 18
TVA_defaut = 20
prix_TTC = Calculer_prix_ttc(prix_HT, TVA_defaut)


print(f"{prix_HT} euros HT = {prix_TTC} euros TTC avec une TVA de {TVA_defaut} % ")

