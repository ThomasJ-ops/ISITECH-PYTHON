
import platform
import psutil
import socket
from colorama import Fore, init

# Initialize colorama so colors work on Windows terminals
init(autoreset=True)

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

def afficher_cpu():
	"""
	Affiche l'utilisation du CPU
	"""
	
	print(f"{gestion_couleur(psutil.cpu_percent(interval=1))} Utilisation CPU: {psutil.cpu_percent(interval=1)}%")
def verifier_systeme():
	"""
	Vérifie si le système est compatible avec le script
	"""
	if platform.system() != "Windows":
		print("Navré ce logiciel ne fonctionne que sur les PC windows")
		exit()
		
	else:
		print("Système compatible détecté")
		
	
	
		
print(f"{verifier_systeme()}")


print(f"{afficher_cpu()}")



