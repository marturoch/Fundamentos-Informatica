#Ejercicio 4
#Escribí un programa que dado un diccionario cuyos valores son listas de 
# números, cree otro diccionario con las mismas claves, pero donde los valores 
# sean una lista de números donde se potencia un número por el siguiente, 
# tomándolos de a pares. Para ser más claros miremos este ejemplo donde si un 
# diccionario es:

#dict1 = {"a": [1,3,5,2], "b": [4,2,3,3]}
#el diccionario resultante debería ser:

#dict2 = {"a": [1, 25], "b": [16, 27]}
#Esto se obtiene al hacer 1 al cubo (el primer par de la lista "a"), y 5 al 
# cuadrado, por un lado; y 4 al cuadrado y 3 al cubo por el otro. Se considera que la cantidad de elementos en las listas siempre es par, por lo que no habría que hacer ninguna comprobación al respecto. Se puede usar el dict1 como diccionario de muestra, pero considerá que la lista puede ser más grande. Por último hay que 
# convertir este último diccionario en un DataFrame de Pandas.
import pandas as pd

dict1 = {"a": [1,3,5,2], "b": [4,2,3,3]}
dict2 = {}
for clave, valor in dict1.items():
    primero = []
    segundo = []
    for pos in range(len(valor)):
        if pos%2 == 0: #par
            primero.append(valor[pos])
        else:
            segundo.append(valor[pos])
    resultado = []
    for i in range(len(primero)):
        resultado.append(primero[i] ** segundo[i])
    dict2[clave] = resultado
print(dict2)

df = pd.DataFrame(dict2)
print(df)

