#Desafio 3. ¿Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero? Reescribí la función incorporando una declaración try-except
#def division(numero, divisor):
    #try:
        #return (numero / divisor)
    #except: #except calcula todos los tipos de errores
        #print("oops hoy estoy quemada")

#Se puede especificar el error que buscamos
def division(numero, divisor):
    try:
        return (numero / divisor)
    except ZeroDivisionError:
        print("oops hoy estoy quemada")
print(division(4,2))
print(division(2,0))
