#1 Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
import re 
texto = input("Ingrese un texto:")
patron = "[a-zA-Z0-9]"
alfanumerico = re.search(patron, texto)

if alfanumerico is not None:
    print("Por lo menos hay un caracter permitido en este texto")
else:
    print("Este texto no tiene ni un caracter permitido")
