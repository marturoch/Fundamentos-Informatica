#2. Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).
numero = int(input("Ingrese un numero:"))
par = (numero%2 == 0)
if numero > 0:
    if par:
        print(numero, "es positivo y par")
    else:
        print(numero, "es positivo e impar")
elif numero < 0:
    if par:
        print(numero, "es negativo y par")
    else:
        print(numero, "es negativo e impar")
else:
    print("es 0 y por lo tanto par")