import psutil
import socket


import psutil
import socket

def main():
    # On récupère toutes les interfaces réseau de l’ordinateur
    interfaces = psutil.net_if_addrs()

    # On parcourt chaque interface (ex : Ethernet, Wi-Fi…)
    for nom_interface, liste_adresses in interfaces.items():

        # On parcourt chaque adresse trouvée pour cette interface
        for adresse in liste_adresses:

            # On vérifie si c’est bien une adresse IPv4
            if adresse.family == socket.AF_INET:
                print("Interface :", nom_interface)
                print("  Adresse IP :", adresse.address)
                print("  Masque     :", adresse.netmask)
                print()

if __name__ == "__main__":
    main()



