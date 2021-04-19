#7. Realizá un programa que encuentre un string 
# que contenga solamente letras minúsculas, 
# mayúsculas, espacios y números.
import re 
string1 = "Hola me llamo Martuy tengo 19"
string2 = "$%^&*"
def letras_numeros_espacios(string):
    return not bool(re.search('[^(a-zA-Z0-9(\s))]',string)) #Si alguno de los caracteres del string no cumple con esta condicion, esto me da verdadero

if letras_numeros_espacios(string1):
    print("El primer texto contiene solamente letras minusculas, mayusculas, espacios o numeros")
else:
    print("El primer texto no contiene solamente letras minusculas, mayusculas, espacios o numeros")

if letras_numeros_espacios(string2):
    print("El segundo texto contiene solamente letras minusculas, mayusculas, espacios o numeros")
else:
    print("El segundo texto no contiene solamente letras minusculas, mayusculas, espacios o numeros")