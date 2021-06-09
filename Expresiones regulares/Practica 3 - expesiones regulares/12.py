#12. Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).
import re 
texto = "Lista de Supermercado: Papa-Batata_Calabaza, Queso, Tomate"
patron = "[-\s_:]"
print(re.sub(patron, "|", texto))