#Ejercicio 2
#Realizá un programa que compare (si son mayores, menores o iguales) los elementos de dos series de números de Pandas.

#Series de muestra:

#[3, 7, 9, 14, 25], [1, 7, 10, 16, 19]

import pandas as pd
serie1 = pd.Series([3, 7, 9, 14, 25])
serie2 = pd.Series([1, 7, 10, 16, 19])
def comparar(serie1, serie2):
    print(serie1 > serie2)
    print(serie1 < serie2)
    print(serie1 == serie2)
print(comparar(serie1,serie2))
