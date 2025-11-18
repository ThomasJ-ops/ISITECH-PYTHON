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
import platform 
import socket
from colorama import Fore, Style, init 


# Initialiser colorama 
init(autoreset=True) 

##Variables


# Définir vos fonctions ici

## Fonction Systeme
def afficher_systeme():
    """
    Affiche les informations système
    """
    print(f"Nom du PC:  {socket.gethostname()} --  {socket.gethostbyname(socket.gethostname()
    )}")  ## Information Nom PC + Adresse IP
    print(f"Système d'exploitation:  {platform.system()}, {platform.version()}") ## Information Windows + build
    print(f"processeur: {platform.processor()}, {platform.machine()}")  ## Information Processeur 
    
    ## information Batterie
    print(f"Batterie en charge : {psutil.sensors_battery().power_plugged}")  ## Information Batterie en charge ou non
    if psutil.sensors_battery().percent < 50:
        print (Fore.GREEN + f"La batterie est actuellement à : {psutil.sensors_battery().percent} %")
    elif 50 <= psutil.sensors_battery().percent <= 80:
        print (Fore.YELLOW + f"La batterie est actuellement à : {psutil.sensors_battery().percent} %")
    else: print (Fore.RED + f"La batterie est actuellement à : {psutil.sensors_battery().percent} %")
    print(f"Votre batterie peut encore tenir {psutil.sensors_battery().secsleft // 60} minutes")  ## Information Temps restant batterie en minutes
    

## Fonction Python

def afficher_python():
    """
    Affiche les informations Python
    """

    print(f"information python : {platform.python_build()}")   ## Information Version Python
    print(f"Compilleur python :  {platform.python_compiler()}")  ## Information Compilateur Python
  

## Fonction pour le CPU

def afficher_cpu(): 
    """
    Affiche toutes les informatoins du CPU
    """
    ## Pourcentage d'utilisation global du CPU
    if psutil.cpu_percent(interval=1) < 50:
        print (Fore.GREEN + f" utilisation CPU : {psutil.cpu_percent(interval=1)} %")
    elif 50 <= psutil.cpu_percent(interval=1) <= 80:
        print (Fore.YELLOW + f" utilisation CPU : {psutil.cpu_percent(interval=1)} %")
    else: print (Fore.RED + f" utilisation CPU : {psutil.cpu_percent(interval=1)} %")

    ## Nombre de coeur physique et logique, fréquence actuelle / max du processeur
    print(f" Nombre de coeur physique: {psutil.cpu_count(logical = False)}") 
    print(f" Nombre de coeur Logique : {psutil.cpu_count(logical = True)}")
    print(f" Fréquence du processeur: {psutil.cpu_freq()}")
    

## Fonction pour la mémoire RAM

def afficher_ram():
    """
    Affiche toutes les informations de la RAM
    """
    ## Mémoire totale, utilisée, libre
    print(f" Mémoire totale: {psutil.virtual_memory().total / (1024 ** 3):.2f} Go")
    print (f" Mémoire utilisée: {psutil.virtual_memory().used / (1024 **3):.2f} Go")
    print (f" Mémoire libre: {psutil.virtual_memory().free / (1024 **3):.2f} Go")

    ## Pourcentage d'utilisation
    if psutil.virtual_memory().percent < 50:
        print (Fore.GREEN + f" Mémoire utilisée à : {psutil.virtual_memory().percent} %")
    elif 50 <= psutil.virtual_memory().percent <= 80:
        print (Fore.YELLOW + f" Mémoire utilisée à : {psutil.virtual_memory().percent} %")
    else: print (Fore.RED + f" Mémoire utilisée à : {psutil.virtual_memory().percent} %")

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

    ## Pourcentage d'utilisation
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
    
    ## Pourcentage d'utilisation
    if psutil.disk_usage("D:\\").percent < 50:
        print(Fore.GREEN + f" Disque D: utilisé à : {psutil.disk_usage("D:\\").percent} %")
    elif 50 <= psutil.disk_usage("D:\\").percent <= 80:
        print(Fore.YELLOW + f" Disque D: utilisé à : {psutil.disk_usage("D:\\").percent} %")
    else: print(Fore.RED + f" Disque D: utilisé à : {psutil.disk_usage("D:\\").percent} %")


## Fonction applications

def afficher_applications():
    """
    Affiche les informations des applications en cours d'exécution
    """
    print(f" le nombre de processus en cours est de : {len(psutil.pids())}")

## Fonction réseau

def afficher_reseau():
    """
    Affiche les informations réseau
    """
    ## Affiches les différentes interfaces réseaux avec leurs IP et leurs Submask
 
    
    # On récupère toutes les interfaces réseau de l’ordinateur
    interfaces = psutil.net_if_addrs()
    # On parcourt chaque interface 
    for nom_interface, liste_adresses in interfaces.items():

        # On parcourt chaque adresse trouvée pour cette interface
        for adresse in liste_adresses:

            # On vérifie si c’est bien une adresse IPv4
            if adresse.family == socket.AF_INET:
                print("Interface :", nom_interface)
                print("  Adresse IP :", adresse.address)
                print("  Masque     :", adresse.netmask)
                print()

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
print("Information Système")
print("=====================================")
print("")
print(f"{afficher_systeme()}")
print("=====================================")
print("Information Python")
print("=====================================")
print("")
print(f"{afficher_python()}")
print("")
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
print("")
print("--- Informatoin applications ---")
print(f"{afficher_applications()}")
print("")
print("--- Information reseau ---")
print(f"{afficher_reseau()}")






