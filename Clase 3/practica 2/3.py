#3. Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la cara opuesta de un dado. Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.
numero = int(input("Ingrese un numero del 1 al 6:"))
if numero >=1 and numero <=6:
    print(7 - numero)
else:
    print("el numero ingresado es incorrecto")