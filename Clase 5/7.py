#7. Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.
path = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt'
with open(path, 'r') as file:
    texto = file.read()
    print(texto)
    palabras = texto.split()
    print(palabras)
    mas_larga = len(max(palabras, key=len))
    print(mas_larga)
    for i in palabras:
        if len(i) == mas_larga:
            print(str(i) + " es la palabras mas larga y tiene " + str(mas_larga) + " caracteres")