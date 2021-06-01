#Ejercicio 5
#Realizá un programa que verifique si una columna dada se 
# encuentra presente en un DataFrame.
import pandas as pd
df = pd.DataFrame({1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]})
#las columnas son 1,2,3
def columna(df, columna):
    presente = columna in df.columns
    return("La columna " + str(columna) + " se encuentra en el Dataframe?: " + str(presente))
print(columna(df,1)) 
#La columna 1 se encuentra en el Dataframe?: True
print(columna(df,"A"))
#La columna A se encuentra en el Dataframe?: False