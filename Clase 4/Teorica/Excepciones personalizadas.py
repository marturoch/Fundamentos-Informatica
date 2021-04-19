def check_int_type(x):
    if type(x) != int:
        raise TypeError("Only integers are allowed")
#definimos un metodo que chequea si una variable en particular es un entero, y me devuelve un error si no lo es.
check_int_type(4)
check_int_type(0.3) 
# me devuelve:
#Traceback (most recent call last):
  #File "c:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 4\Teorica\Excepciones personalizadas.py", line 6, in <module>
    #check_int_type(0.3)
  #File "c:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 4\Teorica\Excepciones personalizadas.py", line 3, in check_int_type
    #raise TypeError("Only integers are allowed")
#TypeError: Only integers are allowed -> este es el que arme
