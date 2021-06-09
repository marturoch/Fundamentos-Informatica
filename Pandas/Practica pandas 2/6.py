#Ejercicio 6
#Escribí un programa que dado dos diccionarios genere dos 
# DataFrame y los una tanto en el eje de las columnas como 
# en el eje de las filas.
import pandas as pd
uno = {1: ["a", "b", "c"], 2: ["d","e","f"]}
dos = {"a": [1, 2, 3], "b": [4,5,6], "c": [7,8,9]}
df1 = pd.DataFrame(uno)
df2 = pd.DataFrame(dos)

columnas = pd.concat([df1,df2])
filas = pd.concat([df1,df2], axis=1)

print(df1)
#   1  2
#0  a  d
#1  b  e
#2  c  f
print(df2)
#  a  b  c
#0  1  4  7
#1  2  5  8
#2  3  6  9
print(columnas)
#     1    2    a    b    c
#0    a    d  NaN  NaN  NaN
#1    b    e  NaN  NaN  NaN
#2    c    f  NaN  NaN  NaN
#0  NaN  NaN  1.0  4.0  7.0
#1  NaN  NaN  2.0  5.0  8.0
#2  NaN  NaN  3.0  6.0  9.0
print(filas)
#   1  2  a  b  c
#0  a  d  1  4  7
#1  b  e  2  5  8
#2  c  f  3  6  9