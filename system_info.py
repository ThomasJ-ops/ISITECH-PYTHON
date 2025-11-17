##Import Librairies
import socket
import platform

##Variables
Nom_PC = socket.gethostname()   ## Information Nom PC
Adresse_IP = socket.gethostbyname(Nom_PC)   ## Information Adresse IP
Architecture_processeur = platform.machine()    ## information Architecture processeur
Systeme = platform.system(), platform.version()   ## Information Windows + build
Processeur = platform.processor()   ## Information Processeur 


Info_Python = platform.python_build()   ## Information Version Python
Info_Python_Compiler = platform.python_compiler()   ## Information Compilateur Python


##Affichage:
print("")
print("=====================")
print("Information Système")
print("=====================")
print("")
print("Nom du PC: ", Nom_PC, "--", Adresse_IP)
print("processeur", Processeur, Architecture_processeur)
print("Système d'exploitation: ", Systeme)
print("")
print("=====================")
print("Information Python")
print("=====================")
print("")
print("information python :", Info_Python)
print("Compilleur python : ", Info_Python_Compiler)



