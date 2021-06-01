#10. Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.
archivo_nuevo = r"C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\nuevo archivo.txt"
import glob
import os 
os.chdir(r"C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 5\versos de prueba")
files_list = glob.glob("*.txt")
with open(archivo_nuevo, "a") as f:
    for file in files_list:
        with open(file, "r") as g:
            f.write(g.read())