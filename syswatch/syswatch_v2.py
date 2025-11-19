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

## Import des différentes fonctions

from collector import collecter_info_systeme
from collector import collecter_cpu
from collector import collecter_memoire
from collector import collecter_disques
from collector import collecter_tout

# Import des modules

import platform


# définitions des différentes variables

info_sys = collecter_info_systeme()
info_cpu = collecter_cpu()
info_ram = collecter_memoire()
info_disque = collecter_disques()
info_all = collecter_tout()


## Définition des fonctions

## Vérification si système compatible

def verifier_systeme():
    """
    Vérifie si le système est compatible avec le script
    """
    if platform.system() != "Windows":
        print("Navré ce logiciel ne fonctionne que sur les PC windows")
        exit()
    else:
        print("Système compatible détecté")

## Afficher info système

def afficher_info_systeme(information_systeme):
    """
    Importe les information système provenant de collector.py
    """
    for cle, valeur in information_systeme.items():
        print(f"{cle}  --  {valeur}")


## afficher info cpu


def afficher_info_cpu(information_cpu):
    """
    Importe les information CPU
    """
    for cle, valeur in information_cpu.items():
        print(f"{cle}  --  {valeur}")


## afficher info ram


def afficher_info_ram(information_ram):
    """
    Importe les information RAM
    """
    for cle, valeur in information_ram.items():
        print(f"{cle}  --  {valeur}")


## afficher info disque


def afficher_info_disque(information_disque):
   """
   Importe les information de disque
   """

   for i in information_disque:
      for cle, valeur in i.items():
         print(f"{cle}  --  {valeur}")
      print("-----------------------------------")

## Programme principale

def afficher_tout():
   """
   Affiche l'intégralitée des infirmations
   """
   verifier_systeme()

   print("=" * 50)
   print( "Programme Syswatch V2" )
   print("=" * 50)
   print("Information système")
   print("-" * 30)
   afficher_info_systeme(info_sys)
   print("-" * 30)
   print("Information CPU")
   print("-" * 30)
   afficher_info_cpu(info_cpu)
   print("-" * 30)
   print("Information RAM")
   print("-" * 30)
   afficher_info_ram(info_ram)
   print("-" * 30)
   print("Information disque")
   print("-" * 30)
   afficher_info_disque(info_disque)


# afficher_info_systeme(info_sys)
# print("")
# afficher_info_cpu(info_cpu)
# print("")
# afficher_info_ram(info_ram)
# print("")
# afficher_info_disque(info_disque)
# print("")

afficher_tout()
