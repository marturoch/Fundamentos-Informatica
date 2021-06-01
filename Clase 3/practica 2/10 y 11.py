#10.Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).
contadores = {} #hago diccionario
cadena = input("Escribi una cadena:")

for caracter in cadena: 
    if caracter in contadores:
        contadores[caracter]+=1
    else:
        contadores[caracter]=1
print(contadores)

for llave, valor in contadores.items():
    print(llave, valor)

#11.Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.

contadores = {}
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in alfabeto + alfabeto.upper():
    contadores[letra] = 0  #agrega todas las letras al diccionario contadores y les pone valor 0 

cadena = input("Escribi una cadena:")

for caracter in cadena:
    if caracter.lower() in alfabeto: #si el caracter de la cadena esta dentro de alfabeto, se le agrega un 1 a ese caracter y deja de ser 0 
        contadores[caracter]+=1

for campo, valor in contadores.items():
    print(campo, valor)
