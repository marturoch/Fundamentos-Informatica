#3. Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.
path = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt'
with open(path, 'r') as file:
    lista = file.readlines() #guarda las lineas del archivo en una lista
    print(lista) 
def imprimir_ultimas(n):
    contador = 0
    a = n-(n-1) 
    print("Las ultimas " + str(n) + " lineas de atras para adelante son:")
    while contador < n:
        print(lista[-(a)])
        contador+=1
        a+=1
imprimir_ultimas(4)
#lo hice para que imprima las ultimas n lineas contando de atras para adelante.
'''
Me devuelve:
['Tuve en mi pago en un tiempo\n', 'Hijos, hacienda y mujer, Pero empecÃ© a padecer,\n', 'Me echaron a la frontera\n', 'Â¡Y quÃ© iba hallar al volver!\n', 'Tan sÃ³lo hallÃ© la tapera. ']
las ultimas 3 lineas de atras para adelante son:
Tan sÃ³lo hallÃ© la tapera.
Â¡Y quÃ© iba hallar al volver!
Me echaron a la frontera
'''
    
