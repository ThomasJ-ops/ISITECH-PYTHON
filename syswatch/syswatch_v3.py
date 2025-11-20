import csv
import os
import json
import time


from collector import collecter_tout

#Variables

donnees = collecter_tout()
Fichier_CSV = "Export_data_systeme.csv"
extract_donnees = []


# Fonctions

#Reecriture à plat de toutes les donnees pour l'export CSV
def mise_a_plat():
    """
    Mise à plat de toutes les données
    """
    donnees = collecter_tout()
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

# Export CSV

def export_CSV():

    with open('syswatch/Export_data_systeme.csv', 'a', newline='') as f:
        colonnes = ["TimeStamp" , "hostname" , "Pourcentage_CPU_utilise" , "RAM_total" , "RAM_Utilise" , "RAM_Libre" , "Pourcentage_RAM_utilise" , "point_montage" , "disque_total" , "disque_utilise" , "pourcentage_disque_utilise"]
        writer = csv.DictWriter(f, fieldnames=colonnes)

        if os.stat('syswatch/Export_data_systeme.csv').st_size != 0:
            writer.writerows(extract_donnees)  # Écrire toutes les lignes
        else:
            writer.writeheader()  # Écrire en-têtes 
            writer.writerows(extract_donnees)  # Écrire toutes les lignes

# Export JSON

def export_json():
    """
    Export des donnees dans un fichier JSON

    """
    with open("syswatch/config.json", "w") as f:
        json.dump(donnees, f, indent=2)

# Fonction export en continue

def collecter_en_continu(intervalle, nombre=0):
    """
    Permet de collecter en continues les données et de les exporter.
    intervall = int temps d'intervalle entre deux collectes
    nombre = le nombre de fois que la fonction affiche et exporte les données. (par défaut infinie)
    """

    compteur = 0
    global donnees, extract_donnees 
    while True:
        time.sleep(intervalle) ## fonction d'interval
        compteur = compteur + 1
        print("collecte ", compteur)  
        donnees = collecter_tout() # rappel donnees
        print(donnees)  #affiche les donnees
        extract_donnees.clear()    # reinitialise les donnees
        mise_a_plat()
        export_CSV()
        export_json()


        if compteur != 0 and compteur >= nombre:    #condition nommbre de collecte
            print("Collecte treminée")
            break
        #else:
            #continue

        ## fonction d'attente d'intervalle
        









    
if __name__ == "__main__":
    # Code exécuté si le module est lancé directement
    collecter_en_continu(2 , 5)
    

    




