import platform
import psutil
import socket
import csv
import os
from colorama import Fore, init
from datetime import datetime


#from collector import collecter_tout

donnees = collecter_tout()

# Initialize colorama so colors work on Windows terminals
init(autoreset=True)


"""

"""


#print(donnees)
extract_donnees = []
for i in donnees["Info_Disque"]:
    ligne = {
        "TimeStamp": donnees.get("TimeStamp"),
        "hostname": donnees["Information_systeme"].get("hostname"),
        "Pourcentage_CPU_utilise": donnees["Info_CPU"].get("Pourcentage_CPU_utilise"),
        "RAM_total": donnees["Info_RAM"].get("RAM_total"),
        "RAM_Utilise": donnees["Info_RAM"].get("RAM_Utilise"),
        "RAM_Libre": donnees["Info_RAM"].get("RAM_Libre"),
        "Pourcentage_RAM_utilise": donnees["Info_RAM"].get("Pourcentage_RAM_utilise"),
        "point_montage": i.get("point_montage"),
        "disque_total": i.get("disque_total"),
        "disque_utilise": i.get("disque_utilise"),
        "pourcentage_disque_utilise": i.get("pourcentage_disque_utilise"),
    }
    extract_donnees.append(ligne)


Fichier_CSV = "Export_data_systeme.csv"

with open('Export_data_systeme.csv', 'a', newline='') as f:
    colonnes = ["TimeStamp" , "hostname" , "Pourcentage_CPU_utilise" , "RAM_total" , "RAM_Utilise" , "RAM_Libre" , "Pourcentage_RAM_utilise" , "point_montage" , "disque_total" , "disque_utilise" , "pourcentage_disque_utilise"]
    writer = csv.DictWriter(f, fieldnames=colonnes)

    if os.stat('Export_data_systeme.csv').st_size != 0:
        writer.writerows(extract_donnees)  # Écrire toutes les lignes
    else:
        writer.writeheader()  # Écrire en-têtes 
        writer.writerows(extract_donnees)  # Écrire toutes les lignes


    

#print(donnees)
    




