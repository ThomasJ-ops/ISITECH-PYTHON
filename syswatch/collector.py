"""
    #### Module collector.py

1. **Fonction collecter_info_systeme()**
   - Retourne un dictionnaire avec :
     - Clé 'os' : système d'exploitation
     - Clé 'version' : version du système
     - Clé 'architecture' : architecture
     - Clé 'hostname' : nom de machine
   - Ne fait pas d'affichage, seulement retourne les données

2. **Fonction collecter_cpu()**
   - Retourne un dictionnaire avec :
     - 'coeurs_physiques'
     - 'coeurs_logiques'
     - 'utilisation' (pourcentage)
   - Utilisez `interval=1` pour une mesure sur 1 seconde

3. **Fonction collecter_memoire()**
   - Retourne un dictionnaire avec :
     - 'total' (en octets)
     - 'disponible' (en octets)
     - 'pourcentage'

4. **Fonction collecter_disques()**
   - Retourne une liste de dictionnaires
   - Chaque dictionnaire représente une partition avec :
     - 'point_montage'
     - 'total' (octets)
     - 'utilise' (octets)
     - 'pourcentage'
   - Ignorez les partitions inaccessibles (try/except)

5. **Fonction collecter_tout()**
   - Appelle toutes les fonctions précédentes
   - Retourne un dictionnaire global avec toutes les métriques structurées
   - Ajoutez une clé 'timestamp' avec la date/heure actuelle (utilisez datetime)

"""

# Imports
import psutil
import platform 
import socket
import datetime
from colorama import Fore, Style, init 


# Initialiser colorama 
init(autoreset=True) 

## Fonctions

def gestion_couleur(pourcentage):
     
	"""
	Retourne une couleur selon le pourcentage
	rouge : > 75%
	orange : 50% - 75%
	vert : < 50%
	"""
	if pourcentage < 40:
		return Fore.GREEN
	elif pourcentage < 75:
		return Fore.YELLOW
	else:
		return Fore.RED    

def gestion_couleur_batterie(pourcentage):
	"""
	Retourne une couleur selon le pourcentage
	rouge : > 75%
	orange : 50% - 75%
	vert : < 50%
	"""
	if pourcentage < 20:
		return Fore.RED
	elif pourcentage < 75:
		return Fore.GREEN
	else:
		return Fore.YELLOW    

def collecter_info_systeme():
    """
    Collecte les informations système de base
    Retourne un dictionnaire avec les informations système
    """
    batterie = psutil.sensors_battery()
    if not batterie.power_plugged:
        Temps_charge = batterie.secsleft // 60
    else:
        Temps_charge = None  # ou 0, ou "En charge"
    



    Info_systeme = {}

    Info_systeme = {
        "os": platform.system(),
        "version": platform.version(),
        "architecture": platform.machine(),
        "hostname": socket.gethostname(),
        "batterie_en_charge" : psutil.sensors_battery().power_plugged,
        "Etat_batterie" : gestion_couleur_batterie(psutil.sensors_battery().percent) + str(psutil.sensors_battery().percent) + "%",
        "Charge_restante": f"{Temps_charge} minutes restantes" if Temps_charge is not None else "En charge"    
}


    return Info_systeme

def collecter_cpu():

    """
    Collecte les informations CPU
    Retourne un dictionnaire avec les informations CPU
    """
    Info_cpu = {}
    Info_cpu = {
        "coeurs_physiques" : psutil.cpu_count(logical=False),
        "coeurs_logiques" : psutil.cpu_count(logical=True),
        "Pourcentage utilisé": gestion_couleur(psutil.cpu_percent(interval=1)) + str(psutil.cpu_percent(interval=1)) + "%",
    }
        
    return Info_cpu

def collecter_memoire():
    """
    Collecte les informations mémoire
    Retourne un dictionnaire avec les informations mémoire
    """

    Info_memoire = {}
    Info_memoire = {
        "total": str(round(psutil.virtual_memory().total / (1024 ** 3),2)) + " Go",
        "Utilisé": str(round(psutil.virtual_memory().used / (1024 **3),2)) + " Go",
        "Libre": round(psutil.virtual_memory().free / (1024 **3),2),
        "Pourcentage utilisé": gestion_couleur(psutil.virtual_memory().percent) + str(psutil.virtual_memory().percent) + " %",
    }
    return Info_memoire

def collecter_disques():
    """
    Collecte les informations des disques
    Retourne une liste de dictionnaires avec les informations des disques
    """

    Info_disques = []
    Partition_pc = psutil.disk_partitions()
    
    for i in Partition_pc:
        try:
            usage = psutil.disk_usage(i.mountpoint)
            Info_disques.append({
                "point_montage": i.device,
                "total": str(round(usage.total / (1024 ** 3),2)) + " Go",
                "utilise": str(round(usage.used / (1024 **3),2)) + " Go",
                "pourcentage d'utilisé": gestion_couleur(usage.percent) + str(usage.percent) + "%",
            })

        except PermissionError:
            continue

    return Info_disques

def collecter_tout():
    """
    Collecte toutes les informations des fonctions précédentes tout en indiquant l'heure
    """
    Info_total = {}
    from datetime import datetime



    Info_total = {
        "Information_systeme" : collecter_info_systeme(),
        "Info_CPU" : collecter_cpu(),
        "Info_RAM": collecter_memoire(),
        "Info_Disque" : collecter_disques(),
        "TimeStamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return Info_total
       




"""
print(collecter_info_systeme())
print(collecter_cpu())
print(collecter_memoire())
print(collecter_disques())
"""
#print(f" voici le total: {collecter_tout()}")


if __name__ == "__main__":
    # Code exécuté si le module est lancé directement
    print(f" voici le total: {collecter_tout()}")
