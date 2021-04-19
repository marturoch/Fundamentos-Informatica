#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.
#una  forma:
import re
with open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt', 'r') as file:
    text = file.read()
    patron = "a"
    if re.search(patron, text) is not None:
        nuevo_texto = re.sub(patron,"a\n", text)      
    path2 = (r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\nuevo verso.txt')
    with open(path2,'w') as miarch:
        miarch.write(nuevo_texto)
#otra forma:
with open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt', 'r') as file:
    text = file.read()
    path2 = (r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\nuevo verso.txt')
    with open(path2,'w') as miarch:
        nuevo_texto = text.replace('a', 'a\n')
        miarch.write(nuevo_texto)
'''
El nuevo texto que me da es:
Tuve en mi pa
go en un tiempo
Hijos, ha
cienda
 y mujer, 
Pero empecé a
 pa
decer,
Me echa
ron a
 la
 frontera

¡Y qué iba
 ha
lla
r a
l volver!
Ta
n sólo ha
llé la
 ta
pera
.
'''
