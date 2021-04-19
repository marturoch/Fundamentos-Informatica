#4. Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
path = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt'
with open(path, 'r') as file:
    text = file.read()
    palabra = text.split()
    print("hay " + str(len(palabra)) + " palabras en este texto.")