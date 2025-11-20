def octets_vers_go(octets): 
    """Convertit des octets en gigaoctets""" 
    go = octets / (1024 ** 3)
    return round(go, 2) 

# Test 
memoire = 8589934592  # 8 Go en octets 
print(f"Mémoire: {octets_vers_go(memoire)} Go") 
# Affiche: Mémoire: 8.0 Go  
