bio = open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Bio.txt','r')
print(bio.readline())#imprime la primer linea y devuelve un string.En este caso "me llamo Martina"
print(bio.read())#imprime el texto (en este caso como ya leyo la primera linea lee lo que queda, es decir, 
'''
Tengo 19
Estoy en mi segundo  año de facultad estudiando Negocios Digitales en UCEMA.
'''
print(bio.readlines())#imrpime las lineas restantes y devuele una lista. En este caso la lista es vacia porque ya llego todo.
bio.close()

print("\n")
bio = open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Bio.txt','r')
print(bio.readline()) #Me llamo Martina.
print(bio.readline()) #Tengo 19.
print(bio.readlines()) #['Estoy en mi segundo año de facultad estudiando Negocios Digitales en UCEMA.']
bio.close()