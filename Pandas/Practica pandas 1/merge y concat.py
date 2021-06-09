import pandas as pd
path = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\personas_2011.csv'
df = pd.read_csv(path, sep=";") #estan seprados por coma 
path2 = r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\ref_categoria_conicet.csv'
df_cat = pd.read_csv(path2, sep=";") 

#print(df.info()) #21 columnas, 68552 valores
#print(df_cat.info()) #2 columnas, 14 valores
df3 = pd.merge(df, df_cat, on='categoria_conicet_id')
df4 = pd.concat([df, df_cat])

#print(df3.info()) #22 columnas, 48640 valores (19912??)

#print(df4) #van a haber 685522 + 14 = 68566 valores
#print(df4.info()) #68566 valores, 22 columnas porque 
#son las 21 del primer df de las cuales una columna la comparten, 
# + la columna del def_cat que no comparten.

#print(df)
#print(df_cat)
#print(df3)
print(df4)