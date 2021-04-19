#7. Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.
path = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt'
with open(path, 'r') as file:
    texto = file.read()
    print(texto)
    palabras = texto.split()
    palabras_sin_coma = []
    for i in palabras:
        palabra = i.strip(",") #esto es porque hay palabras que tienen seguida una coma y hay que sacarla porque cuenta como caracter.
        palabras_sin_coma.append(palabra)
    print(palabras_sin_coma)
    mas_larga = len(max(palabras_sin_coma, key=len))
    print(mas_larga)
    for i in palabras_sin_coma:
        if len(i) == mas_larga:
            print(str(i) + " es la palabras mas larga y tiene " + str(mas_larga) + " caracteres")