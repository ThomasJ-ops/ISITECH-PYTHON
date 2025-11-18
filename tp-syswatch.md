# Projet Fil Rouge : SysWatch
## Outil de surveillance système en Python

---

## Introduction

SysWatch est un outil de monitoring système que vous allez développer progressivement tout au long de la formation. Ce projet fil rouge vous permettra d'appliquer immédiatement les concepts vus en cours.

L'objectif est de créer une application complète capable de :
- Collecter des métriques système (CPU, RAM, disques)
- Organiser le code de manière professionnelle
- Traiter et exporter les données
- Persister l'historique dans une base de données
- Fournir une interface en ligne de commande

---

## Objectifs pédagogiques

- Appliquer les concepts Python dans un contexte réel
- Comprendre l'évolution d'un projet de script simple à application structurée
- Utiliser les modules de la bibliothèque standard
- Pratiquer la programmation orientée objet
- Gérer la persistance des données

---

## Prérequis techniques

**Installation de psutil**

La bibliothèque psutil permet d'accéder aux informations système. Installez-la avec :

```bash
pip install psutil
```

**Structure du projet**

Créez un dossier `syswatch` pour votre projet. Vous y ajouterez des fichiers au fur et à mesure.

---

## Partie 1 : Collecte basique (Jour 1)

### Objectif

Créer un premier script Python capable d'afficher les informations système de base.

### Fichier à créer

`syswatch_v1.py`

### Consignes

1. **Importations nécessaires**
   - Importez le module `platform` pour les informations système générales
   - Importez le module `psutil` pour les métriques détaillées

2. **Fonction d'affichage des informations système**
   - Créez une fonction qui affiche :
     - Le système d'exploitation
     - La version du système
     - L'architecture (32 ou 64 bits)
     - Le nom de la machine (hostname)
     - La version de Python utilisée

3. **Fonction d'affichage CPU**
   - Nombre de coeurs physiques
   - Nombre de coeurs logiques
   - Pourcentage d'utilisation actuel
   - Utilisez `psutil.cpu_count()` et `psutil.cpu_percent()`

4. **Fonction d'affichage mémoire**
   - Mémoire totale en Go (arrondi à 2 décimales)
   - Mémoire disponible en Go
   - Pourcentage d'utilisation
   - Utilisez `psutil.virtual_memory()`
   - Convertissez les octets en gigaoctets (diviser par 1024^3)

5. **Fonction d'affichage disques**
   - Pour chaque partition montée :
     - Point de montage
     - Pourcentage d'utilisation
   - Gérez les erreurs de permission avec try/except
   - Utilisez `psutil.disk_partitions()` et `psutil.disk_usage()`

6. **Point d'entrée**
   - Dans le bloc `if __name__ == "__main__":`
   - Appelez toutes vos fonctions d'affichage
   - Ajoutez un titre et la version du script

### Critères de validation

- Le script s'exécute sans erreur
- Toutes les informations sont affichées clairement
- Les valeurs sont formatées (2 décimales pour les Go et pourcentages)
- Les erreurs de permission sont gérées

### Exemple de sortie attendue

```
=== SysWatch v1.0 ===

=== Système ===
OS: Linux
Version: 5.15.0
Architecture: x86_64
Hostname: dev-server
Python: 3.11.4

=== CPU ===
Coeurs physiques: 4
Coeurs logiques: 8
Utilisation: 23.5%

=== Mémoire ===
Total: 16.00 GB
Disponible: 8.45 GB
Utilisation: 47.2%

=== Disques ===
/ : 65.3% utilisé
/home : 42.1% utilisé
```

---

## Partie 2 : Organisation et modularité (Jour 2)

### Objectif

Restructurer le code en fonctions réutilisables et créer un module dédié.

### Fichiers à créer

- `collector.py` : module de collecte
- `syswatch_v2.py` : script principal amélioré

### Consignes

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

## Partie 3 : Traitement et export (Jour 3)

### Objectif

Ajouter la capacité d'exporter les données et de calculer des statistiques.

### Fichiers à créer/modifier

- `syswatch_v3.py` : script avec export
- `traitement.py` : module de traitement optionnel

### Consignes

#### Export CSV

1. **Fonction exporter_csv(metriques, fichier)**
   - Prend les métriques collectées
   - Les écrit dans un fichier CSV
   - Colonnes suggérées :
     - timestamp
     - hostname
     - cpu_percent
     - mem_total_gb
     - mem_dispo_gb
     - mem_percent
     - disk_root_percent
   - Utilisez le module `csv` avec `DictWriter`
   - Si le fichier existe, ajoutez les données (mode append)
   - Sinon créez-le avec en-têtes

2. **Fonction exporter_json(metriques, fichier)**
   - Sauvegarde les métriques complètes en JSON
   - Utilisez `json.dump()` avec `indent=2`
   - Format lisible pour humains

#### Collecte continue

1. **Fonction collecter_en_continu(intervalle, nombre)**
   - Paramètres :
     - `intervalle` : secondes entre chaque collecte
     - `nombre` : nombre de collectes (0 = infini)
   - À chaque itération :
     - Collecte les métriques
     - Les affiche
     - Les sauvegarde en CSV
   - Permet l'arrêt avec Ctrl+C (gestion KeyboardInterrupt)
   - Utilisez `time.sleep()` pour l'intervalle

#### Statistiques basiques

1. **Fonction calculer_moyennes(fichier_csv)**
   - Lit le fichier CSV d'historique
   - Calcule et retourne :
     - CPU moyen, min, max
     - Mémoire moyenne, min, max
   - Utilisez le module `csv` avec `DictReader`
   - Gérez les conversions de types (str vers float)

2. **Fonction detecter_pics(fichier_csv, seuil_cpu, seuil_mem)**
   - Identifie les moments où :
     - CPU > seuil_cpu
     - OU mémoire > seuil_mem
   - Retourne une liste de dictionnaires avec timestamp et valeurs

#### Programme principal étendu

1. **Arguments en ligne de commande**
   - Sans argument : collecte unique et affichage
   - `--continu` : collecte continue
   - `--intervalle N` : intervalle en secondes
   - `--nombre N` : nombre de collectes
   - `--stats` : affiche statistiques du CSV
   - Utilisez `sys.argv` (simple) ou `argparse` (avancé)

### Critères de validation

- Export CSV fonctionnel avec ajout de données
- Export JSON structuré
- Collecte continue qui s'arrête proprement avec Ctrl+C
- Statistiques correctement calculées
- Arguments ligne de commande fonctionnels

### Exemple d'utilisation

```bash
# Collecte unique
python syswatch_v3.py

# Collecte toutes les 30s, 10 fois
python syswatch_v3.py --continu --intervalle 30 --nombre 10

# Afficher statistiques
python syswatch_v3.py --stats
```

---

## Partie 4 : POO et persistance (Jour 4)

### Objectif

Restructurer l'application avec des classes et ajouter une base de données SQLite.

### Fichiers à créer

- `models.py` : classes de données
- `database.py` : gestion base de données
- `syswatch_final.py` : application finale

### Consignes

#### Fichier models.py

1. **Classe SystemMetrics**
   - Utilisez `@dataclass` (ou constructeur classique)
   - Attributs :
     - timestamp (datetime)
     - hostname (str)
     - cpu_percent (float)
     - memory_total (int en octets)
     - memory_available (int)
     - memory_percent (float)
     - disk_usage (dict ou str)
   - Méthode `to_dict()` : retourne dictionnaire pour JSON/DB
   - Méthode `__str__()` : représentation lisible

2. **Classe SystemCollector**
   - Attribut d'instance : hostname
   - Méthode `collect()` : collecte et retourne objet SystemMetrics
   - Encapsule toute la logique de collecte psutil
   - Gère les erreurs de permission

#### Fichier database.py

1. **Classe MetricsDatabase**
   - Constructeur prend chemin de la base (défaut: "syswatch.db")
   - Méthode privée `_init_schema()` :
     - Crée table metrics si inexistante
     - Colonnes : id, timestamp, hostname, cpu_percent, memory_percent, memory_total, memory_available, disk_usage
     - Crée index sur (timestamp, hostname)
   
2. **Méthode save(metrics: SystemMetrics)**
   - Insère objet SystemMetrics dans la base
   - Utilise `to_dict()` pour extraire les données
   - Paramètres préparés (?) pour éviter injection SQL

3. **Méthode get_latest(hostname, limit=10)**
   - Retourne les N dernières métriques pour un host
   - Ordre décroissant par timestamp
   - Retourne liste de dictionnaires
   - Utilisez `row_factory = sqlite3.Row` pour accès par nom

4. **Méthode get_statistics(hostname, hours=24)**
   - Calcule statistiques sur période
   - Requête SQL avec AVG, MAX, MIN, COUNT
   - Filtre avec WHERE timestamp >= date_limite
   - Utilisez `datetime` et `timedelta` pour calculer date limite

5. **Méthode cleanup_old(days=30)**
   - Supprime entrées plus anciennes que N jours
   - Retourne nombre d'entrées supprimées
   - Utilisez `cursor.rowcount`

#### Fichier syswatch_final.py

1. **Fonction afficher_stats(db, hostname)**
   - Appelle `db.get_statistics()`
   - Affiche de manière formatée
   - Gère le cas où pas de données

2. **Fonction main()**
   - Parse arguments ligne de commande avec `argparse`
   - Arguments :
     - `--collect` : mode collecte continue
     - `--interval N` : intervalle (défaut 60)
     - `--stats` : afficher statistiques
     - `--export FICHIER` : exporter en JSON
     - `--cleanup N` : nettoyer données > N jours
   - Instancie SystemCollector et MetricsDatabase
   - Exécute action demandée

3. **Mode collecte continue**
   - Boucle avec `time.sleep(interval)`
   - À chaque itération :
     - Collecte avec SystemCollector
     - Affiche
     - Sauvegarde avec MetricsDatabase
   - Gère KeyboardInterrupt proprement

### Structure finale du projet

```
syswatch/
├── models.py           # Classes métier
├── database.py         # Accès base de données
├── collector.py        # Collecte psutil (optionnel, peut être dans models)
├── syswatch_final.py   # Script principal
├── syswatch.db         # Base SQLite (créée automatiquement)
└── README.md           # Documentation
```

### Critères de validation

- Architecture orientée objet cohérente
- Base de données SQLite fonctionnelle
- Requêtes SQL correctes (pas d'injection)
- Interface CLI complète avec argparse
- Code organisé et documenté
- Application robuste (gestion erreurs)

---

## Fonctionnalités bonus (optionnel)

### Niveau 1 : Amélioration de l'affichage

1. **Formatage couleurs**
   - Utilisez des codes ANSI pour colorer la sortie
   - Rouge si CPU/RAM > 80%
   - Jaune si > 60%
   - Vert sinon

2. **Graphiques ASCII**
   - Barres de progression pour CPU/RAM
   - Exemple : `[######    ] 60%`

### Niveau 2 : Alertes

1. **Classe AlertManager**
   - Définit seuils (CPU, RAM, disque)
   - Méthode `check(metrics)` retourne liste d'alertes
   - Alertes sauvegardées dans table séparée

2. **Notifications simples**
   - Affichage console avec message clair
   - Optionnel : envoi email avec module `smtplib`

### Niveau 3 : Multi-serveurs

1. **Support configuration**
   - Fichier JSON listant serveurs à monitorer
   - Structure : nom, IP, port SSH, identifiants

2. **Collecte distante**
   - Connexion SSH avec `paramiko`
   - Exécution script distant
   - Récupération et stockage résultats

### Niveau 4 : Interface web

1. **API REST avec Flask**
   - Route `/metrics` : dernières métriques
   - Route `/stats` : statistiques
   - Route `/history` : historique JSON

2. **Dashboard HTML/JavaScript**
   - Page web avec rafraîchissement auto
   - Graphiques avec Chart.js
   - Tableau des dernières métriques

---

## Livrables attendus

### Structure minimale

```
syswatch/
├── models.py
├── database.py
├── syswatch_final.py
├── syswatch.db
└── README.md
```

### Contenu du README.md

1. **Description du projet**
   - Objectif
   - Fonctionnalités

2. **Installation**
   - Prérequis Python
   - Installation dépendances
   - Commandes pip

3. **Utilisation**
   - Exemples de commandes
   - Description des options
   - Exemples de sorties

4. **Architecture**
   - Description des modules
   - Schéma de la base de données

5. **Évolutions futures**
   - Fonctionnalités à ajouter
   - Améliorations possibles

### Code

- Respecte PEP 8 (indentation, nommage, longueur lignes)
- Fonctions documentées (docstrings)
- Gestion des erreurs appropriée
- Code lisible et commenté quand nécessaire

---

## Critères d'évaluation

### Fonctionnalité (40%)

- Toutes les fonctionnalités demandées sont présentes
- L'application fonctionne sans erreur
- Les données collectées sont correctes
- La persistance fonctionne

### Qualité du code (30%)

- Respect des conventions Python (PEP 8)
- Code organisé et modulaire
- Fonctions courtes et ciblées
- Documentation présente (docstrings, README)

### Architecture (20%)

- Utilisation appropriée de la POO
- Séparation des responsabilités
- Organisation logique des fichiers
- Réutilisabilité du code

### Robustesse (10%)

- Gestion des erreurs
- Validation des entrées
- Comportement prévisible
- Messages d'erreur clairs

---

## Conseils de développement

### Approche progressive

1. **Ne pas tout faire d'un coup**
   - Commencez simple (Partie 1)
   - Testez à chaque étape
   - Ajoutez fonctionnalités progressivement

2. **Testez régulièrement**
   - Exécutez votre code après chaque modification
   - Vérifiez que ça fonctionne avant d'ajouter du nouveau

3. **Utilisez git (optionnel mais recommandé)**
   - Commitez après chaque partie fonctionnelle
   - Permet de revenir en arrière si problème

### Debugging

1. **Utilisez print() abondamment**
   - Affichez les valeurs des variables
   - Vérifiez le flux d'exécution

2. **Lisez les messages d'erreur**
   - La dernière ligne indique le type d'erreur
   - Le traceback montre où l'erreur se produit

3. **Simplifiez quand ça ne marche pas**
   - Testez chaque fonction individuellement
   - Utilisez des données de test simples

### Ressources

1. **Documentation Python**
   - docs.python.org pour les modules standard
   - docs.python.org/3/library/sqlite3.html pour SQLite
   - docs.python.org/3/library/argparse.html pour CLI

2. **Documentation psutil**
   - psutil.readthedocs.io pour exemples

3. **Stack Overflow**
   - Recherchez vos erreurs
   - Beaucoup de solutions existent déjà

---

## Timeline suggéré

### Jour 1 - Après-midi

- Installer psutil
- Créer syswatch_v1.py
- Tester collecte de base
- Faire fonctionner toutes les sections

### Jour 2 - Après-midi

- Créer collector.py
- Restructurer en fonctions
- Créer syswatch_v2.py
- Vérifier modularité

### Jour 3 - Après-midi

- Ajouter export CSV
- Implémenter collecte continue
- Ajouter statistiques
- Créer syswatch_v3.py avec arguments

### Jour 4 - Matin

- Créer models.py avec classes
- Créer database.py
- Créer syswatch_final.py
- Tester ensemble
- Rédiger README.md

---

## Questions fréquentes

### Q: Puis-je utiliser d'autres bibliothèques ?

R: Oui pour les bonus. Non pour les parties principales (utilisez stdlib + psutil uniquement).

### Q: Comment gérer les erreurs de permission sur les disques ?

R: Utilisez try/except PermissionError et continuez avec les autres partitions.

### Q: Le timestamp doit être dans quel format ?

R: Format ISO 8601 recommandé (datetime.now().isoformat()).

### Q: Comment tester sans attendre la collecte continue ?

R: Utilisez un intervalle court (5-10 secondes) et un nombre limité (2-3 collectes).

### Q: Que faire si psutil ne s'installe pas ?

R: Vérifiez que pip est à jour (pip install --upgrade pip). Sous Linux, installez python3-dev si nécessaire.

### Q: Les statistiques doivent porter sur quelle période ?

R: Par défaut 24 heures, mais paramétrable.

### Q: Comment structurer le dict disk_usage ?

R: Clés = points de montage, valeurs = dict avec total/used/percent.

### Q: Faut-il gérer les fuseaux horaires ?

R: Non, utilisez l'heure locale simplement.

---

## Ressources complémentaires

### Documentation officielle

- Python: https://docs.python.org/3/
- psutil: https://psutil.readthedocs.io/
- SQLite: https://docs.python.org/3/library/sqlite3.html
- argparse: https://docs.python.org/3/library/argparse.html

### Exemples de commandes utiles

```python
# Tester une requête SQL
import sqlite3
conn = sqlite3.connect("syswatch.db")
cursor = conn.execute("SELECT * FROM metrics LIMIT 5")
print(cursor.fetchall())

# Voir structure table
cursor = conn.execute("PRAGMA table_info(metrics)")
print(cursor.fetchall())

# Compter entrées
cursor = conn.execute("SELECT COUNT(*) FROM metrics")
print(cursor.fetchone()[0])
```

### Patterns utiles

```python
# Context manager pour DB
from contextlib import closing
with closing(sqlite3.connect("db.db")) as conn:
    # Utiliser conn
    pass  # Auto-close

# Gestion KeyboardInterrupt
try:
    while True:
        # Boucle infinie
        pass
except KeyboardInterrupt:
    print("\nArrêt demandé")
finally:
    # Nettoyage
    pass

# Valeur par défaut dict
data = {}
data.setdefault('compteur', 0)
data['compteur'] += 1
```

---
