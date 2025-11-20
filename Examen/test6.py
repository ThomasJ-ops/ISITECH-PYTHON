def formatter_memoire(octets):
    """
    Conversion les octets en fonction de leurs taille
    
        Args:
        octets (int): _description_
    """

    if octets < 1024:
        return str(octets) + " octets"
    elif octets < 1024*2:
        return str(round(octets / 1024, 2)) + " Ko"
    else:
        return str(round(octets / (1024**2), 2)) + " Mo"


print(formatter_memoire(125))

