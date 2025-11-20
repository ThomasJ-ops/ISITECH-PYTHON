import csv
import os


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
    with open('Export_data_systeme.csv', 'a', newline='') as f:
        colonnes = ["TimeStamp" , "hostname" , "Pourcentage_CPU_utilise" , "RAM_total" , "RAM_Utilise" , "RAM_Libre" , "Pourcentage_RAM_utilise" , "point_montage" , "disque_total" , "disque_utilise" , "pourcentage_disque_utilise"]
        writer = csv.DictWriter(f, fieldnames=colonnes)

        if os.stat('Export_data_systeme.csv').st_size != 0:
            writer.writerows(extract_donnees)  # Écrire toutes les lignes
        else:
            writer.writeheader()  # Écrire en-têtes 
            writer.writerows(extract_donnees)  # Écrire toutes les lignes

# Export JSON

def export_json():
    """
    Export des donnees dans un fichier JSON

    """
    
    
    
if __name__ == "__main__":
    # Code exécuté si le module est lancé directement
    mise_a_plat()
    export_CSV()
    




