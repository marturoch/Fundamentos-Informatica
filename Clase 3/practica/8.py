#Realizá un programa que declare tres listas lista1, lista2 y lista3, 
# donde las dos primeras listas deben tener cinco enteros cada una, ingresados por teclado 
# y asigne para cada elemento de la lista3 la suma de los elementos de la lista1 y la lista2 
# (es decir, el primer elemento de la lista3 tiene que ser 
# la suma del primer elemento de la lista1 y el primero de la lista2)
lista1=[]
lista2=[]
lista3=[]
contador=0
while contador < 5:
    n = int(input("ingrese un numero a la primer lista:"))
    lista1.append(n)
    n1 = int(input("ingrese un numero a la segunda lista:"))
    lista2.append(n1)
    contador+=1
posicion_lista1=0
posicion_lista2=0
contador2 = 0
while contador2 < 5:
    suma = lista1[posicion_lista1] + lista2[posicion_lista2]
    lista3.append(suma)
    posicion_lista1+=1
    posicion_lista2+=1
    contador2+=1

print(lista1)
print(lista2)
print(lista3)
