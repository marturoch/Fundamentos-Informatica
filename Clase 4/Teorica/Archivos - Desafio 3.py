#Desafío III: Abrí el archivo bio.txt y escribí una mini biografía de presentación. 
# Para pensar 🤔:¿Cómo darías formato al texto que estas creando?
with open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Bio.txt', 'w') as file:
    file.write("Me llamo Martina. \nTengo 19. \nEstoy en mi segundo año de facultad estudiando Negocios Digitales en UCEMA.")
texto = open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Bio.txt','r')
text = texto.read()
print(text)
texto.close()
#write Abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura
'''
me dio:
Me llamo Martina.
Tengo 19.
Estoy en mi segundo año de facultad estudiando Negocios Digitales en UCEMA.
'''