#Escribir un programa para calcular la nota final de un estudiante, teniendo en cuenta que 
# por cada respuesta correcta el estudiante suma 4 puntos, 
# por cada incorrecta se le resta 1 punto y 
# si la respuesta está en blanco no se le suma ni se le resta.
def nota_final(correctas, incorrectas, blanco):
    nota = (correctas * 4) + (incorrectas * -1)
    return nota
print(nota_final(3,4,7))
