#Ejercicio 3
#Realizá un programa que agregue datos a un DataFrame vacío.
import pandas as pd
#vamos a agregar esto:
# {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
df = pd.DataFrame()
df[1] = [1, 4, 3, 4, 5]
df[2] = [4, 5, 6, 7, 8]
df[3] = [7, 8, 9, 0, 1]
print(df)
#Devuelve:
#   1  2  3
#0  1  4  7
#1  4  5  8
#2  3  6  9
#3  4  7  0
#4  5  8  1