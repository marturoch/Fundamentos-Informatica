bio = open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\creacion de archivos y carpetas para los practicos\Bio.txt', 'r')
print(bio.read())
'''
imprime todo el texto
Me llamo Martina.
Tengo 19.
Estoy en mi segundo año de facultad estudiando Negocios Digitales en UCEMA.
'''
bio = open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\creacion de archivos y carpetas para los practicos\Bio.txt', 'r')
print(bio.readlines())
#imprime las lineas y las devuelve en una lista
#['Me llamo Martina. \n', 'Tengo 19. \n', 'Estoy en mi segundo año de facultad estudiando Negocios Digitales en UCEMA.']['Me llamo Martina. \n', 'Tengo 19. \n', 'Estoy en mi segundo año de facultad estudiando Negocios Digitales en UCEMA.']
