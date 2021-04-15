#4. Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
import re
with open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt', 'r') as file:
    text = file.read()
    print(re.findall("(\n)(\w*)(\n)", text))