#Ejercicio 7
#Creá un programa que dado un diccionario y una lista 
# añada está última al DataFrame generado a partir del 
# diccionario.
import pandas as pd
d1 = {1:[1,2,3], 2:[4,5,6], 3:[7,8,9]}
df = pd.DataFrame(d1)
print(df)
#   1  2  3
#0  1  4  7
#1  2  5  8
#2  3  6  9

lista = ["a", "b", "c"]
def agregar_lista(lista, nombre, df):
    serie = pd.Series(lista, name=nombre)
    return pd.concat([df,serie], axis=1)
print(agregar_lista(lista, 4, df))
#   1  2  3  4
#0  1  4  7  a
#1  2  5  8  b
#2  3  6  9  c

