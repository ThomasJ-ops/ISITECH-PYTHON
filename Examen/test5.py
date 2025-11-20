import psutil   

def collecter_processus_actifs(): 
    """
    Retourne le nombre de processus actifs sur le système
        arg:
            processus = list
    """ 
    processus = []
    processus = psutil.pids()  #attribution de tous les procesuss via pids à la liste processus
    return len(processus)   #on compte le nombre d'éléments dans la liste processus



print(collecter_processus_actifs()) #On affiche le résultat