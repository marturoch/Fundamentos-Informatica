#13. Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
import re 
texto = "Supermercado:Papa-Batata_Calabaza, Queso,Tomate"
patron = "\W"
lista = re.findall(patron, texto)
primero = lista[0]
segundo = lista[1]
texto2= re.sub(primero, "_", texto)
print(re.sub(segundo, "_", texto2))
#PREGUNTAR