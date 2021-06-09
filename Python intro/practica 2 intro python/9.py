#Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir el nombre y la edad de cada alumno por teclado. 
#El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). Al finalizar se deben mostrar los siguientes datos:
#La edad máxima de todos los alumnos
#Los alumnos que tengan la edad máxima
nombres = []
edades = []
nombre = input("Ingrese nombre:")
if nombre != "*":
    nombres.append(nombre)
    edad = int(input("Ingrese su edad:"))
    edades.append(edad)
else:
    print("No hay ningun alumno")

while nombre != "*":
    nombre = input("ingrese nombre:")
    if nombre != "*":
        nombres.append(nombre)
        edad = int(input("Ingrese edad:"))
        edades.append(edad)

edad_max = max(edades) 
print("La edad maxima es:" + str(edad_max))
for i in range(len(edades)):
    if edades[i] == edad_max:
        print(nombres[i] + " " + "tiene" + " " + str(edad_max))