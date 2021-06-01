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

