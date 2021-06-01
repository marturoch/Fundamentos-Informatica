#Ejercicio 2
#Escribí un programa que guarde en una lista una columna 
# de un DataFrame.
#Forma 1
import pandas as pd
df = pd.DataFrame({1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]})
def columna(df, columna):
    for i in df.columns:
        if i == columna:
            print("columna " + str(i) + ":" + str(df[i].to_list()))
columna(df,1)
#Devuelve:
#columna 1:[1, 4, 3, 4, 5]

#forma 2
def columnas(df, columna):
    for i in df.columns:
        if i == columna:
            print("columna " + str(i) + ":" + str(df[i].tolist()))
columnas(df,2)
#Devuelve:
# columna 2:[4, 5, 6, 7, 8]