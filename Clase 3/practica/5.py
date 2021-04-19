#Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.
dia = int(input("Ingrese un día (número) del 1 al 7:"))
if dia >= 1 and dia <= 7:
  if dia == 1:
    print("Es lunes")
  elif dia == 2:
    print("Es martes")
  elif dia == 3:
    print("Es miércoles")
  elif dia == 4:
    print("Es jueves")
  elif dia == 5:
    print("es viernes")
  elif dia == 6:
    print("Es sábado")
  elif dia == 7:
    print("Es domingo")
else:
    print("el numero es incorrecto")
