#Desafio 2. Creá una función denominada mitades que tenga como argumento un número e imprima el resultado de la división de ese número por 2.
#Hacemos funcion division y usamos dos parametros
#Para pensar 🤔: ¿Qué crees que ocurrirá cuando ingresas un 9 como parámetro? ¿Y con un 0?
def division(numero, divisor):
    return (numero / divisor)
print(division(27,9)) #devuelve el resultado de la division
print(division(4,0)) #devuelve ZeroDivisionError , porque no se puede dividir por 0
