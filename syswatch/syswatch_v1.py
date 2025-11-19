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
    print(f"{gestion_couleur(psutil.sensors_battery().percent)}La batterie est actuellement à : {psutil.sensors_battery().percent} %")
    if psutil.sensors_battery().power_plugged == True:
        print("Batterie en charge")
    else:
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
    print(f"{gestion_couleur(psutil.cpu_percent(interval=1))} Utilisation CPU: {psutil.cpu_percent(interval=1)}%")

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
    print(f"{gestion_couleur(psutil.virtual_memory().percent)}Mémoire utilisée à : {psutil.virtual_memory().percent} %")
    

## Fonction pour l'usage du disque

def afficher_disque():
    """
    Affiches toutes les informations des disques C: et D:
    """
    Partition_pc = psutil.disk_partitions()
    # cree une liste de vide qui contiendra toutes les partitions (disques)
    Disque_dur = []
    for i in Partition_pc:
    # ajoute le nom de la partition (disque) a la liste Disque_dur
        Disque_dur.append(i.device)

    for i in Disque_dur:
        print(f" Espace total du disque {i} : {psutil.disk_usage(i).total / (1024 ** 3):.2f} Go")
        print(f" Espace utilisé du disque {i} : {psutil.disk_usage(i).used / (1024 ** 3):.2f} Go")
        print(f" Espace libre du disque {i} : {psutil.disk_usage(i).free / (1024 ** 3):.2f} Go")
        print(f"{gestion_couleur(psutil.disk_usage(i).percent)} Disque {i} utilisée à : {psutil.disk_usage(i).percent} %")
    
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

def gestion_couleur(pourcentage):
	"""
	Retourne une couleur selon le pourcentage
	rouge : > 75%
	orange : 50% - 75%
	vert : < 50%
	"""
	if pourcentage < 50:
		return Fore.GREEN
	elif pourcentage < 75:
		return Fore.YELLOW
	else:
		return Fore.RED    

# Votre code ici
    
    ## Vérification si système compatible
print(f"{verifier_systeme()}")

    ## Affichage des informations
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






