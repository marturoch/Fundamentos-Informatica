#Ejercicio 4
#Escribí un programa que elimine las primeras n filas 
# de un DataFrame. Pista: el DataFrame original no debe 
# modificarse.
import pandas as pd
df = pd.DataFrame({1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]})
def eliminar(df, fila):
    df2 = df.iloc[fila:]
    return df2

print(df)
#   1  2  3
#0  1  4  7
#1  4  5  8
#2  3  6  9
#3  4  7  0
#4  5  8  1
print(eliminar(df,3)) #elimina las primeras 3 filas
#   1  2  3
#3  4  7  0
#4  5  8  1

