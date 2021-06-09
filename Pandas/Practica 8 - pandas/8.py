#Ejercicio 8
#Realizá un programa que dado dos DataFrames genere otro
#  que contenga solo las columnas en común.
import pandas as pd
df1 = pd.DataFrame({1: ["a", "b", "c"], 2: ["d","e","f"]})
df2 = pd.DataFrame({0: [1, 2, 3], 1:[4,5,6], 2:[7,8,9]})
result = pd.concat([df1,df2], join="inner", ignore_index=True)
print(df1)
#   1  2
#0  a  d
#1  b  e
#2  c  f
print(df2)
#   0  1  2
#0  1  4  7
#1  2  5  8
#2  3  6  9
print(result)
#   1  2
#0  a  d
#1  b  e
#2  c  f
#3  4  7
#4  5  8
#5  6  9