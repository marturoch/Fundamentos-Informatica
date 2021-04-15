#8. Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
texto1 = open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso1.txt','r')
text = texto1.read()
print("Contenido texto 1:")
print(text)
texto1.close()

print("\n")
texto2 = open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso2.txt', 'r')
text2 = texto2.read()
print("Contenido texto 2:")
print(text2)
texto2.close()

with open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso de prueba.txt', 'w')as file:
    file.write(text)
    file.write("\n\n")
    file.write(text2)
with open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba\verso de prueba.txt', 'r')as file:
    print("\n")
    print("Contenido texto 3:")
    print(file.read())

 

