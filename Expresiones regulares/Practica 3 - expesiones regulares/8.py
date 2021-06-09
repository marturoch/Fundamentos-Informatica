#8. Escribí un programa que separe y 
# devuelva los caracteres númericos de un string.
import re
string = "1 2 3 4 hola 5 6 7 %^"
patron = "\d"
lista = re.findall(patron, string)
for i in lista:
    print(int(i))