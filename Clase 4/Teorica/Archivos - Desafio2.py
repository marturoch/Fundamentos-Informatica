#Desafío II: Investigá sobre los métodos os.mkdir() y os.listdir()
#os.listdir() → me da una lista con los nombres de los archivos y directorios que estan dentro del directorio indicado (path). 
#os.mkdir() →  agrega un subdirectorio dentro del directorio en el que estoy parado. 
import os
print(os.getcwd())
#me devuelve: 'C:\\Users\\martu\\Documents\\martu\\UCEMA\\2 - PRIMER CUATRI'

#Ahora vamos a cambiar de directorio:
os.chdir('C:\\Users\\martu\\Documents\\martu\\UCEMA\\2 - PRIMER CUATRI\INFORMATICA')
print(os.getcwd())
#me devuelve:'C:\\Users\\martu\\Documents\\martu\\UCEMA\\2 - PRIMER CUATRI\\INFORMATICA'

#os.listdir() me da una lista con los archivos que estan en el directorio donde estoy parado.
print(os.listdir())
#me devuelve ['Bibliografia', 'Clase 1', 'Clase 2', 'Clase 3', 'Clase 5', 'Clase4', 'Informatica (1).zip', 'Python_intro', 'tareas', 'UCEMA_Fundamentos_de_informatica-master']

# os.mkdir() Agrega un diretorio dentro de la carpeta en la que estoy parado.
os.mkdir('nuevo')
print(os.listdir())
# Me devuelve: ['Bibliografia', 'Clase 1', 'Clase 2', 'Clase 3', 'Clase 5', 'Clase4', 'Informatica (1).zip', 'nuevo', 'Python_intro', 'tareas', 'UCEMA_Fundamentos_de_informatica-master']