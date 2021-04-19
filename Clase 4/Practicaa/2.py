#2. Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
import re 
def caracteres_permitidos(string):
    return not bool(re.search('[^a-zA-Z0-9]',string)) #Si alguno de los caracteres del string no cumple con esta condicion, esto me da verdadero

print("el string" , "ABCDEFabcdef123450", "tienen todos los caracteres permitidos?")
print(caracteres_permitidos("ABCDEFabcdef123450"))
print("el string", "*&@#!}{", "tiene todos los caracteres permitidos?")
print (caracteres_permitidos("*&@#!}{"))