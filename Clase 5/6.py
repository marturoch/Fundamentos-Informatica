#6. Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
#forma 1:
import re
path = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso3.txt'
with open(path, 'r') as file:
    text = file.read()
    lista = re.findall("\n", text)
    texto_nuevo = text.replace('\n', '')
    path2 = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\texto sin saltos de linea.txt'
    with open(path2, 'w') as file:
        file.write(texto_nuevo)