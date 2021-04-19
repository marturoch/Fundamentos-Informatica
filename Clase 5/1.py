#1. Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
'''
texto (voy a usar el mismo para todos los ejercicios.)
Tuve en mi pago en un tiempo 
Hijos, hacienda y mujer, Pero empecé a padecer,
Me echaron a la frontera
¡Y qué iba hallar al volver!
Tan sólo hallé la tapera. 
'''
#forma 1: 
import re
path = r"C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\creacion de archivos y carpetas para los practicos\texto de prueba.txt"
with open(path,"r") as file:
    contador = 0 
    for i in file:
        if re.search('^[^T]', i) is not None:
            contador +=1
    print("Hay " + str(contador) + " lineas que no empiezan con la letra T")

#forma 2:
with open(path, 'r') as miarch:
    conta = 0 
    for i in miarch:
        if i[0] != "T":
            conta += 1
print("Hay " + str(conta) + " lineas que no empiezan con la letra T")
