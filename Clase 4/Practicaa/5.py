#5 Escribí un programa que diga si 
# un string empieza con un número específico.
import re 
string = "10 y 24 son mis numeros favoritos"
patron = "^10"
if re.search(patron, string) is not None:
    print("El string comienza con el numero 10.")
else:
    print("El string no comienza con el numero 10.")

