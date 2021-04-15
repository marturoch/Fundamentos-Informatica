#2. Escribí un programa que lea un archivo e imprima las primeras n líneas.
import re
with open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt', 'r') as file:
    n = 0
    while n < 3:
        print(file.readline())
        n+= 1



