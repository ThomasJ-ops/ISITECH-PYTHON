import csv

# Écrire CSV
donnees = [
    {"serveur": "web-01", "cpu": 45, "ram": 60},
    {"serveur": "web-02", "cpu": 80, "ram": 70},
    {"serveur": "db-01", "cpu": 50, "ram": 95}
]

with open("metriques.csv", "w", newline='') as f:
    # DictWriter : écrit dicts en CSV
    colonnes = ["serveur", "cpu", "ram"]
    writer = csv.DictWriter(f, fieldnames=colonnes)
    
    writer.writeheader()  # Écrire en-têtes
    writer.writerows(donnees)  # Écrire toutes les lignes
"""
# Lire CSV
with open("metriques.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['serveur']}: CPU {row['cpu']}%")
"""
"""
# Writer basique (listes)
with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Nom", "Valeur"])  # En-tête
    writer.writerow(["test1", 42])
    writer.writerow(["test2", 99])

"""   
"""
# Reader basique
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Sauter en-tête
    for row in reader:
        nom, valeur = row
        print(f"{nom} = {valeur}")

# Dialectes CSV
with open("excel.csv", "w", newline='') as f:
    writer = csv.writer(f, dialect='excel')  # Format Excel
    # ou delimiter=';', quotechar='"'

"""