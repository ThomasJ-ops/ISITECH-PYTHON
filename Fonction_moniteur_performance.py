"""
 Fonctionnalités à implémenter
 Votre script doit afficher les informations suivantes :
 1. Utilisation du CPU
 Pourcentage d'utilisation global du CPU
 Nombre de cœurs physiques et logiques
 Fréquence actuelle du processeur
 2. Utilisation de la mémoire RAM
 Mémoire totale disponible
 Mémoire utilisée
 Mémoire disponible
 Pourcentage d'utilisation
 3. Utilisation du disque
 Espace total de chaque partition
 Espace utilisé
 Espace libre
 Pourcentage d'utilisation
 4. Informations réseau (bonus)
 Statistiques d'envoi et de réception de données
 Nombre de connexions actives
 5. Affichage coloré
 Utilisez des couleurs différentes selon les niveaux d'utilisation :
 Vert : < 50%
 Jaune : 50% - 80%
 Rouge : > 80%
 """

# Imports
import psutil 
from colorama import Fore, Style, init 


# Initialiser colorama 
init(autoreset=True) 

# Définir vos fonctions ici

## Fonction pour le CPU

def afficher_cpu(): 
    """
    Affiche toutes les informatoins du CPU
    """
    print(f" utilisation CPU : {psutil.cpu_percent(interval=1)} %")
    print(f" Nombre de coeur physique: {psutil.cpu_count(logical = False)}") 
    print(f" Nombre de coeur Logique : {psutil.cpu_count(logical = True)}")
    print(f" Fréquence du processeur: {psutil.cpu_freq()}")



## Fonction pour la mémoire RAM
def afficher_ram():
    """
    Affiche toutes les informations de la RAM
    """

    print(f" Mémoire totale: {psutil.virtual_memory().total / (1024 ** 3):.2f} Go")
    print (f" Mémoire utilisée: {psutil.virtual_memory().used / (1024 **3):.2f} Go")
    print (f" Mémoire libre: {psutil.virtual_memory().free / (1024 **3):.2f} Go")
    print (f" Mémoire utilisée à : {psutil.virtual_memory().percent} %")

## Fonction pour l'usage du disque
def afficher_disque():
    """
    Affiches toutes les informations des disques C: et D:
    """
##Information lecteur C:
    print("Lecteur C: ")
    print(f" Espace total du disque C: : {psutil.disk_usage("C:\\").total / (1024 ** 3):.2f} Go")
    print(f" Espace utilisé du disque C: : {psutil.disk_usage("C:\\").used / (1024 ** 3):.2f} Go")
    print(f" Espace libre du disque C: : {psutil.disk_usage("C:\\").free / (1024 ** 3):.2f} Go")
    if psutil.disk_usage("C:\\").percent < 50:
        print(Fore.GREEN + f" Disque C: utilisé à : {psutil.disk_usage("C:\\").percent} %")
    elif 50 <= psutil.disk_usage("C:\\").percent <= 80:
        print(Fore.YELLOW + f" Disque C: utilisé à : {psutil.disk_usage("C:\\").percent} %")
    else: print(Fore.RED + f" Disque C: utilisé à : {psutil.disk_usage("C:\\").percent} %")

##Information lecteur D:
    print("Lecteur D: ")
    print(f" Espace total du disque D: : {psutil.disk_usage("D:\\").total / (1024 ** 3):.2f} Go")
    print(f" Espace utilisé du disque D: : {psutil.disk_usage("D:\\").used / (1024 ** 3):.2f} Go")
    print(f" Espace libre du disque D: : {psutil.disk_usage("D:\\").free / (1024 ** 3):.2f} Go")
    if psutil.disk_usage("D:\\").percent < 50:
        print(Fore.GREEN + f" Disque D: utilisé à : {psutil.disk_usage("D:\\").percent} %")
    elif 50 <= psutil.disk_usage("D:\\").percent <= 80:
        print(Fore.YELLOW + f" Disque D: utilisé à : {psutil.disk_usage("D:\\").percent} %")
    else: print(Fore.RED + f" Disque D: utilisé à : {psutil.disk_usage("D:\\").percent} %")

## Gestion de la couleur selon le pourentage

    

# Votre code ici
    

#pass 


"""

def afficher_memoire(): 
# Votre code ici 
pass 
def afficher_disque(): 
# Votre code ici 
pass 
def choisir_couleur(pourcentage): 
# Retourne une couleur selon le pourcentage 
pass 
def main(): 
# Programme principal 
pass 
if __name__ == "__main__": 
    main() 
"""

print("=====================================")
print("Moniteur de performance")
print("=====================================")
print("")
print("--- CPU ---")
print(f"{afficher_cpu()}")
print("")
print("--- Mémoire RAM ---")
print(f"{afficher_ram()}")
print("")
print("--- Utilisation Disque ---")
print(f"{afficher_disque()}")




