import psutil 
import platform 

"""
    Création d'un script pour récupérer les données réseaux et OS d'un ordinateur
"""

def get_network_info(): 
    """Récupértion des informations réseau (nombre de bytes envoyé et reçu)

        arg: 
            sent = un float des données envoyées
            Recv = un float des données envoyées
    """

    net=psutil.net_io_counters() 
    Sent=net.bytes_sent/1024/1024 
    Recv=net.bytes_recv/1024/1024 
    print("Envoyé:",Sent,"Mo") 
    print("Reçu:",Recv,"Mo") 
    return Sent,Recv 

def show_info(): 
    """
    Fonction de récupération du système d'opération
    arg: 
        os = Str
    """ 

    os=platform.system() 
    print("OS:",os) 


if __name__ == "__main__":
   get_network_info()
   show_info() 