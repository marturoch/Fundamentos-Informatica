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
print(type(columnas))
#unido = pd.concat([columnas,df2], axis=1)
#print(unido)