#Ejercicio 7
#Escribí un programa que obtenga las 3 primeras filas de un DataFrame dado.
import pandas as pd
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df = pd.DataFrame(datos_ejemplo, index=labels)
print(df.head(3))
#     nombre  puntaje  intentos  califica
#a  Agustina     12.5         1         1
#b     Diana      9.0         3         0
#c     Karen     16.5         2         1

#Ejercicio 8
#Realizá un programa que seleccione e impirma las columnas "nombre" y
#  "puntaje" del DataFrama anterior.
print(df['nombre'])
#a    Agustina
#b       Diana
#c       Karen
#d      Julián
#e      Emilio
#f      Miguel
#g       Mateo
#h       Laura
#i       Jorge
#j       Lucas
#Name: nombre, dtype: object
print(df['puntaje'])
#a    12.5
#b     9.0
#c    16.5
#d    13.0
#e     9.0
#f    20.0
#g    14.5
#h    10.0
#i     8.0
#j    19.0
#Name: puntaje, dtype: float64

#Ejercicio 9
#Escribí un programa que dado el DataFrame anterior imprima 
# los nombres en mayúscula y la longitud de los mismos en 
# una nueva tabla.
nombres = df['nombre'].tolist()
nombres_mayus = []
longitud = []
for i in nombres:
    nombres_mayus.append(i.upper())
    longitud.append(len(i))
serie = pd.Series(longitud, nombres_mayus)
#el primero va en la segunda columna, el segundo en la primer columna
print(serie)
#AGUSTINA    8
#DIANA       5
#KAREN       5
#JULIÁN      6
#EMILIO      6
#MIGUEL      6
#MATEO       5
#LAURA       5
#JORGE       5
#LUCAS       5
#dtype: int64
df = pd.DataFrame(serie)
print(df)