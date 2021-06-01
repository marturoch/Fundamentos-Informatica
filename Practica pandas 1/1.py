#Ejercicio 1
#Escribí un programa que sume, reste, multiplique y divida dos series de números de Pandas.

#Series de muestra:

#[3, 7, 12, 15, 21], [1, 4, 10, 14, 19]
import pandas as pd
serie1 = pd.Series([3, 7, 12, 15, 21])
serie2 = pd.Series([1, 4, 10, 14, 19])
def operaciones(serie1, serie2):
    print(serie1 + serie2)
    print(serie1 - serie2)
    print(serie1 / serie2)
    print(serie1 * serie2)
print(operaciones(serie1, serie2))
