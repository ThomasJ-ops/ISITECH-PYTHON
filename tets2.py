import platform
import psutil
import socket
from colorama import Fore, init

# Initialize colorama so colors work on Windows terminals
init(autoreset=True)


if psutil.sensors_battery().power_plugged == True:
    print("Batterie en charge")
else:
    print(f"Votre batterie peut encore tenir {psutil.sensors_battery().secsleft // 60} minutes")  ## Information Temps restant batterie en minutes


## print(f"{psutil.sensors_battery().secsleft // 60}")