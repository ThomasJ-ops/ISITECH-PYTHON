import psutil 
def lister_disques(): 
    
    
    partitions = psutil.disk_partitions() 
    for p in partitions:
        try: 
            usage = psutil.disk_usage(p.mountpoint) 
            print(f"{p.mountpoint}: {usage.percent}%")
        except PermissionError:
            print(f"Vous navez pas les droits pour afficher les informations de partition de {p.mountpoint}") 
lister_disques() 
# Erreur: PermissionError sur certaines partitions