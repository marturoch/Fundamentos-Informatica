#Ejercicio en grupo I - Compra de una casa
#El programa debe calcular cuantos meses tomaría ahorrar el dinero necesario para pagar el depósito. 
# Este programa debe preguntarle al usuario cual es su sueldo anual, que porcentaje del sueldo quiere ahorrar por mes 
# y cual es el costo de la casa en cuestión.
costo_total = int(input("Ingrese el costo total de la propiedad:"))
sueldo_anual = int(input("Ingrese su sueldo anual:"))
porcentaje_ahorrado = float(input("Ingrese la proporcion de sueldo que quiere ahorrar mensualmente:"))
deposito = costo_total * 0.25
cantidad_ahorrada = 0
tasa_interes = 0.04
tasa_mensual = tasa_interes/12
sueldo_mensual= sueldo_anual/12
ahorro_mensual = sueldo_mensual * porcentaje_ahorrado
print(deposito)
print(sueldo_mensual)
print(ahorro_mensual)
r = tasa_mensual
mes = 0
ahorros = 0
while ahorros <= deposito:
  mes += 1
  ahorros += ahorro_mensual
  ahorros = ahorros * (1 + r)
print("En " + str(mes) + " meses lograrias ahorrar la suma de: $" + str(int(ahorros)) + ", alcanzando asi el total del deposito")
ganancia = ahorros - (ahorro_mensual*mes)
print("\nObtuviste una ganancia de: $"+str(int(ganancia)))
'''
Lo probamos con:
Costo total = 9.000.000
#sueldo anual = 1.500.000
#proporcion sueldo = 0.3
'''