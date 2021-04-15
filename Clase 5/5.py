#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.
import re
with open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt', 'r') as file:
    text = file.read()
    patron = "a"
    if re.search(patron, text) is not None:
        print(re.sub(patron,"a\n", text))
