def celsius_vers_fahrenheit(celsius): 
    """Convertit des degrés Celsius en Fahrenheit""" 
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit 


def fahrenheit_vers_celsius(fahrenheit): 
    """Convertit des degrés Fahrenheit en Celsius""" 
    celsius = (fahrenheit - 32) * 5/9 
    return celsius 

# Utilisation
#  
temp_c = 25 
temp_f = celsius_vers_fahrenheit(temp_c) 
print(f"{temp_c}°C = {temp_f}°F") 




temp_f2 = 77 
temp_c2 = fahrenheit_vers_celsius(temp_f2) 
print(f"{temp_f2}°F = {temp_c2:.1f}°C") 