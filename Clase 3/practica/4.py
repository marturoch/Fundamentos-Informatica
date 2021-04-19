#Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, América del Norte, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla:
#Zona	Ubicación	Costo/gramo
#1	América del Sur	10.00 dólares
#2	América Central	15.00 dólares
#3	América del Norte	18.00 dólares
#4	Europa	24.00 dólares
#5	Asia	30.00 dólares
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. 
# Realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.
gramos = int(input("Ingrese el peso en gramos:"))
zona = input("ingrese la zona:")
if gramos < 5000:
    if zona == "America del Sur":
        print("El cobro por la entrega del paquete es de:" + "" + str(10 * gramos))
    elif zona == "America Central":
        print("El cobro por la entrega del paquete es de:" + "" + str(15 * gramos))
    elif zona == "America del Norte":
        print("El cobro por la entrega del paquete es de:" + "" + str(18 * gramos))
    elif zona == "Europa":
        print("El cobro por la entrega del paquete es de:" + "" + str(24 * gramos))
    elif zona == "Asia":
        print("El cobro por la entrega del paquete es de:" + "" + str(30 * gramos))
else:
    print("Su paquete fue rechazado")

