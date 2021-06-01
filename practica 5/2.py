#2. Escribí un programa que lea un archivo e imprima las primeras n líneas.
path = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt'
import re
def primeras_lineas(numero):
    with open(path, 'r') as file:
        contador = 0
        while contador < numero:
            print(file.readline())
            contador+= 1
primeras_lineas(3)