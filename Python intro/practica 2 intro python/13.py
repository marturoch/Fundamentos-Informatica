#Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función esMultiplo.
entero = int(input("ingresa un numero entero:"))
entero2 = int(input("ingresa otro numero entero:"))
def esMultiplo(entero, entero2):
    if entero2%entero == 0:
        print(entero2, "es multiplo de", entero)
    elif entero%entero2 == 0:
        print(entero, "es multiplo de", entero2)
    else:
        print("ninguno es multiplo de ninguno")
esMultiplo(entero, entero2)