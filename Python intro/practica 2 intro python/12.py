#Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. 
# Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves 
# serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno. 
# El programa tiene que pedir el número de alumnos que se va a introducir, 
# luego su nombre y sus notas hasta que introduzcamos un número negativo. 
# Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. 
# Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.
alumnos = []
diccionario = {}
nombres = []
contador = 0

cantidad =int(input("Cuantos alumnos va a ingresar?:"))
while contador < cantidad:
    contador+=1
    nombre = input("Ingrese el nombre del alumno:")
    if nombre not in nombres:
        nombres.append(nombre)
        nota = int(input("Ingrese la nota:"))
        if nota > 0:
            diccionario[nombre]=[nota]
            nota = int(input("Ingrese la otra nota:"))
            if nota > 0:
                diccionario[nombre].append(nota)
                while nota > 0:
                    nota = int(input("Ingrese la otra nota: "))
                    if nota > 0:
                        diccionario[nombre].append(nota)                
            alumnos.append(diccionario)
        diccionario = {}
    else:
        print("Este alumno ya se ingreso")
contador=0
print(nombres)
print(alumnos)
for alumno in alumnos: 
    for key in alumno.keys():
        print("El promedio de " + str(key) + " es: " + str(sum(alumno[key]) / len(alumno[key])))