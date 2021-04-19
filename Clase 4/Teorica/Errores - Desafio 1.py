#Desafio I: Descargá y ejecutá el script1_manejo_errores.py
#Para pensar 🤔: ¿Qué tipo de error se obtiene al ejecutar el programa? ¿En dónde se encuentra el error? ¿Cómo te das cuenta?

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d)/(2*a) #el que tiene error
sol2 = (-b+cmath.sqrt(d))/(2*a) 

print('The solution are {0} and {1}'.format(sol1,sol2))

'''
  File "c:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\Clase 4\Teorica\Errores - Desafio 1.py", line 18
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    ^
SyntaxError: invalid syntax
'''
#Me doy cuenta del error porque este se encuentra en el elemento que precede a la flecha. en este caso el fin de la línea anterior a la 18.

#Para corregirlo:
# sol1 = (-b-cmath.sqrt(d)/(2*a) #el que tiene error
# sol1 = (-b+cmath.sqrt(d)/(2*a)) #sin error