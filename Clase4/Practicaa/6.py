#6. Escribí un programa que dada una lista de strings 
# verifique si se encuentran en una frase dada.
import re
lista_strings = ["hoy", "sol", "pileta","amigos"]
frase = "Hoy tomamos sol en la playa con mis amigos"
for i in lista_strings:
    patron = i
    if re.search(patron, frase) is not None:
        print("la palabra " + r"'" + i + r"'" " se encuentra en la frase dada")
    else:
        print("la palabra " + r"'" + i + r"'" " no se encuentra en la frase dada")