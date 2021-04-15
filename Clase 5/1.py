#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
import re
with open(r"C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\texto de prueba.txt","r") as file:
    lineas = file.readlines()
    contador = 0 
    for i in lineas:
        if re.search('^[^M]', i) is not None:
            contador +=1
            print(i)
    print("\n")
    print("Hay " + str(contador) + " lineas que no empiezan con la letra M")
