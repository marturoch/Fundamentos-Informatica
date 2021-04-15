#6. Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
import re

texto = open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt', 'r')
text = texto.read()
patron = "\n"
lista = re.findall(patron, text)
print(re.sub(patron, "", text))

with open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\saltos de linea.txt', 'w') as file:
    file.write(lista[0])
    file.write(lista[1])
    file.write(lista[2])
    file.write(lista[3])
    file.write("fin")
texto2_read = open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\saltos de linea.txt', 'r')
print(texto2_read.read())


    
