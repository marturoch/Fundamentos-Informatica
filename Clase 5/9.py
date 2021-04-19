#9. Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay 
# en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en 
# cuestión con respecto a la cantidad total de palabras.
path = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt' 
with open(path, 'r') as file:
    texto = file.read()
    palabras = texto.split()
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    for palabra in frecuencias:
        frecuencia = frecuencias[palabra]
        print("La palabra " + r"'"+ str(palabra) + r"'"+ " tiene una frecuencia de " + str(frecuencia))