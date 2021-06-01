#6. Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.
minutos = int(input("ingrese una cantidad de minutos: "))
horas = minutos // 60 
mins = minutos%60 
print(str(minutos), "minutos", "son", str(horas), "horas y", str(mins), "minutos")