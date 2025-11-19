"""
    #### Script syswatch_v2.py

1. **Importation du module**
   - Importez votre module `collector`

2. **Fonctions d'affichage**
   - Créez des fonctions pour afficher chaque section
   - Ces fonctions prennent en paramètre les dictionnaires retournés par collector
   - Exemple : `afficher_cpu(data_cpu)`

3. **Fonction de conversion**
   - Créez une fonction `octets_vers_go(octets)` qui convertit et formate
   - Retourne une chaîne avec 2 décimales : "16.00 GB"

4. **Programme principal**
   - Appelez `collecter_tout()`
   - Affichez toutes les sections de manière structurée

### Critères de validation

- Séparation claire entre collecte (collector.py) et affichage (syswatch_v2.py)
- Les fonctions sont documentées (docstrings)
- Le code est réutilisable
- Pas de variables globales (sauf constantes)

---
"""


## Import de la fonction collecter_tout de collector.py

from collector import collecter_tout

##print(collecter_tout())


## Définition des fonctions

def afficher_info_systeme(data_systeme):
    """Importe les information système provenant de collector.py

    Args:
        data_systeme (_type_): _description_
    """
    return information_systeme()

print(afficher_info_systeme())







