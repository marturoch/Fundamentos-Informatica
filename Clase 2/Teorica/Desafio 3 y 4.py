#Desafío III: Probá las lineas anteriores y anotate para qué sirve cada uno de los métodos y funciones.
saludo = "Hola mundo"
print(len(saludo)) # cuenta la cantidad de caracteres en el string. En este caso 10.
print(saludo.upper()) #hace los caracteres del string mayuscula
print(saludo.lower()) #hace los caracteres del string minuscula
print(saludo.count('o')) #cuenta la cantidad de lo que le pasemos en el parametro. En este caso cuenta la cantidad de "o".
print(saludo.replace('o','a')) #reemplaza todas las ocurrencias del primer parametro por el segundo. 

#Para pensar 🤔: ¿Se podrán combinar los métodos? Probá hacer saludo.upper().lower() ¿Qué dá? ¿Por qué?
print(saludo.upper().lower()) #primero lo hace mayuscula y despues minuscula. Devuelve el string en minuscula.

#Desafío IV: Vimos que el método replace nos permite reemplazar un caracter por otro de un string dado, 
# pero nos dejará reemplazar un segemento más largo? 
# Probá hacer saludo.replace("mundo", "terricolas")
print(saludo.replace("mundo", "terricolas")) #funciona

#Para pensar 🤔: ¿Si imprimís saludo luego de ejecutar la linea anterior qué obtenés? ¿Cambió el valor de la variable?
print(saludo) #no cambia el valor de la variable porque los strings son inmutables. Si queremos que cambie el valor hay que crear una nueva variable.
#ejemplo: saludo_mayus = saludo.upper()

#No hay desafio 5.