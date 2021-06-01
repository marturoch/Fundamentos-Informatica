#4. Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).
import re 
string = "hola_hola"
patron = "\w*_\w*"
print(re.findall(patron, string))