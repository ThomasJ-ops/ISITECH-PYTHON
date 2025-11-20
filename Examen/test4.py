import psutil

def collecter_cpu(): 
    infos = {} 
    infos['coeurs_physiques'] = psutil.cpu_count(logical=False) 
    infos['coeurs_logiques'] = psutil.cpu_count(logical=True) 
    infos['utilisation'] = psutil.cpu_percent(interval=1) 
    return infos 

resultat = collecter_cpu() 

print(f"CPU: {resultat['utilisation']}%") 
# Affiche toujours: CPU: 0.0%  (même quand CPU est chargé!)

