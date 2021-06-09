import pandas as pd
lista = [3, 7, 12, 15, 21]
serie1 = pd.Series(data=lista)

lista = [3, 7, 12, 15, 21]
serie2 = pd.Series(lista)

serie3 = pd.Series([3, 7, 12, 15, 21])

serie4 = pd.Series(data=lista, index=['a','b','c','d','e'])
print(serie1)
print(serie2)
print(serie3)
print(serie4)

info = {"a":1, "b":2, "c":3, "d":4}
serie5 = pd.Series(data=info, index=['a', 'b', 'c', 'd']) #no hace falta ponerle el index, no cambia sigue igual
serie6 = pd.Series(data=info, index=['0','1', '2', '3'])
print(serie5)
print(serie6)

