#9. Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay 
# en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en 
# cuestión con respecto a la cantidad total de palabras.
path = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt' 
with open(path, 'r') as file:
    texto = file.read()
    palabras = texto.split()
    palabras_sin_coma = []
    for i in palabras:
        palabra = i.strip(",")
        palabras_sin_coma.append(palabra)
    cantidad_palabras = len(palabras_sin_coma)
    frecuencias = {}
    for palabra in palabras_sin_coma:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    for palabra in frecuencias:
        frecuencia = frecuencias[palabra] / cantidad_palabras
        print("La palabra "+ str(palabra) + " tiene una frecuencia de " + str(frecuencia))
