#Ejercicio 3
#Escribí un programa para convertir un diccionario a una serie de Pandas.

#Diccionario de muestra:
import pandas as pd
dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
serie1 = pd.Series(dict1)
print(serie1)