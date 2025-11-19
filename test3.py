import platform
import psutil
import socket
from colorama import Fore, init
from datetime import datetime

# Initialize colorama so colors work on Windows terminals
init(autoreset=True)

# Affiche la date et l'heure courante au format lisible
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
