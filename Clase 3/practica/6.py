#Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.
#Recordá que la manera de copiar una lista en otra es:
#lista2 = list(lista1)
palabra1 = input("Ingrese una palabra:")
palabra2 = input("Ingrese una palabra:")
palabra3 = input("Ingrese una palabra:")
palabra4 = input("Ingrese una palabra:")
palabra5 = input("Ingrese una palabra:")
lista = []
lista = [palabra1, palabra2, palabra3, palabra4, palabra5]
lista2 = list(lista)
lista2.reverse()
print(lista2)
