import platform
import psutil
import socket
from colorama import Fore, init
from datetime import datetime

# Initialize colorama so colors work on Windows terminals
init(autoreset=True)

from collector import collecter_disques
from collector import collecter_cpu

list_disque = collecter_disques()
list_cpu = collecter_cpu()




    

#print(list_disque)
#print(list_cpu)



