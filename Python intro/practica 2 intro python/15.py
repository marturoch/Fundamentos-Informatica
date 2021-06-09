# Creá un programa para gestionar datos de los socios de un club, el cual permita:

# Cargar la información de los socios en un diccionario para acceder por número de socio. Los datos que se deben almacenar son: número, 
# nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al dia (s/n) (el programa tiene que dejar de cargar cuando se ingrese el número 0). 
# El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

# Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día
# Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día
# Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día

# Informar la cantidad de socios que tiene el club.
# Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.
# Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.
# Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
# Imprimir el listado de socios completos.
# Definir las funciones que creas necesarias.

#FUNCIONES

#IMPRIMIR SOCIOS
def listado_socios(ingreso):
    if ingreso == 1:
        for socio in socios:
            print(socio["Nombre y Apellido"])

#BORRAR UN SOCIO
def dar_de_baja(ingreso):
    if ingreso == 1:
        nombre = input("Ingrese el nombre completo del socio que quiere dar de baja:")
        for socio in socios:
            if socio["Nombre y Apellido"] == nombre:
                list.remove(socios, socio)  
        listado_socios(1)

#PEDIR NUMERO SEGUN NOMBRE
def pedir_id(nombre):
    for socio in socios:
        if socio["Nombre y Apellido"] == nombre:
            print("El ID de " + nombre + " es: " + str(socio["Numero"]))

#ACTUALIZAR ESTADO DE PAGO
def actualizar_estado_de_pago(numero):
    for socio in socios:
        if socio["Numero"] == numero:
            print("Estado actual de pago: " + socio["Cuota al dia"])
            socio["Cuota al dia"] = input("Ingrese Si o No, si tiene la cuota al dia:")
            print(socio)

#PEDIR DATOS SEGUN NUMERO
def pedir_datos(numero):
    for socio in socios:
        if socio["Numero"] == numero:
            print(socio)

# Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.
def nueva_fecha(fecha_i, fecha_f):
    for socio in socios:
        if socio["Fecha de ingreso"] == fecha_i:
            socio["Fecha de ingreso"] = fecha_f
            print(socio)

#PREGUNTAR SI TIENE CUOTA AL DIA
def estado_cuota(numero):
    for socio in socios:
        if socio["Numero"] == numero:
            if socio["Cuota al dia"] == "Si":
                print("La cuota se encuentra paga")
            else: 
                print("La cuota no se encuentra paga")

#INGRESAR SOCIO
dic = {}
dic1 = {}

def ingreso_socios(ingreso):
    if ingreso == 1:
        nombre = input("Ingrese su nombre y apellido:")
        if nombre != "0":
            ingreso = input("Ingrese la fecha de ingreso:")
            cuota = input("Ingrese si tiene la cuota al dia:")
            numero = len(socios) + 1
            dic["Numero"]=numero
            dic["Nombre y Apellido"]=nombre
            dic["Fecha de ingresoo"]=ingreso
            dic["Cuota al dia"]=cuota
            dic["Numero"]=numero
            socios.append(dic)
            while nombre != "0":
                nombre = input("Ingrese su nombre y apellido:")
                if nombre != "0":
                    ingreso = input("Ingrese la fecha de ingreso:")
                    cuota = input("Ingrese si tiene la cuota al dia:")
                    numero = len(socios) + 1
                    dic1["Numero"]=numero
                    dic1["Nombre y Apellido"]=nombre
                    dic1["Fecha de ingresoo"]=ingreso
                    dic1["Cuota al dia"]=cuota
                    dic1["Numero"]=numero
                    socios.append(dic1)    
        listado_socios(1)
    
#PROGRAMA

socios = [
            { "Numero": 1, "Nombre y Apellido": "Florencia Ocampo", "Fecha de ingreso": "14/09/2001", "Cuota al dia": "Si"}, 
            { "Numero": 2, "Nombre y Apellido": "David Estévez", "Fecha de ingreso": "14/09/2001", "Cuota al dia": "Si"}, 
            { "Numero": 3, "Nombre y Apellido": "Sofía Cáceres", "Fecha de ingreso": "21/10/2017", "Cuota al dia": "Si"},
]

login = int(input("Para ingresar al sistema pulse 1, de lo contrario pulse 0: "))

if login==1:
    print("\nCargar Socio: 0\nDar de baja: 1\nConsultar ID: 2\nConsultar situacion de pago: 3\nActualizar estado de pago: 4\nTus datos: 5\nCambiar fecha: 6\nLista de socios: 7")
    print("\nCantidad de socios actual: " + str(len(socios)))
    
    opcion = int(input())
        
    if opcion==0:
        ingreso_socios(int(input("Pulse 1 para cargar un nuevo socio: ")))
    elif opcion==1:
        dar_de_baja(int(input("Pulse 1 para eliminar un socio: ")))
    elif opcion==2:
        pedir_id(input("Ingrese el nombre completo: "))
    elif opcion==3:
        estado_cuota(int(input("Ingrese su ID: ")))
    elif opcion==4:
        actualizar_estado_de_pago(int(input("Ingrese su ID: ")))
    elif opcion==5:
        pedir_datos(int(input("Ingrese su ID: ")))
    elif opcion==6:
        nueva_fecha(input("Ingrese la fecha anterior: "), input("Ingrese la fecha nueva: "))
    elif opcion==7:
        listado_socios(1)

else:
    print("Adios...")