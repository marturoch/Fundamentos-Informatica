#8. Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
#una forma
import re
path = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt'
path2 = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso2.txt'
with open(path, 'r') as file:
    with open(path2, 'r') as file2:
        path3 = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso de prueba.txt'
        with open(path3, 'w') as file3:
            for linea in file:
                file3.write(linea)
            for linea in file2:
                file3.write(linea)
#otra forma
path = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt'
texto1 = open(path,'r')
text = texto1.read()
texto1.close()
'''
Texto 1:
Tuve en mi pago en un tiempo
Hijos, hacienda y mujer,
Pero empecÃ© a padecer,
Me echaron a la frontera
Â¡Y quÃ© iba hallar al volver!
Tan sÃ³lo hallÃ© la tapera.
'''
path2 = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso2.txt'
texto2 = open(path2, 'r')
text2 = texto2.read()
texto2.close()
'''
Texto 2:
Sosegao vivÃ­a en mi rancho
Como el pÃ¡jaro en su nido;
AllÃ­ mis hijos queridos
Iban creciendo a mi lao...
SÃ³lo queda al desgraciao
Lamentar el bien perdido.
'''
path_nuevo = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso de prueba.txt'
with open(path_nuevo,'w')as file:
    file.write(text)
    file.write("\n")
    file.write(text2)
'''
Tuve en mi pago en un tiempo
Hijos, hacienda y mujer,
Pero empecÃ© a padecer,
Me echaron a la frontera
Â¡Y quÃ© iba hallar al volver!
Tan sÃ³lo hallÃ© la tapera.
Sosegao vivÃ­a en mi rancho
Como el pÃ¡jaro en su nido;
AllÃ­ mis hijos queridos
Iban creciendo a mi lao...
SÃ³lo queda al desgraciao
Lamentar el bien perdido.
'''