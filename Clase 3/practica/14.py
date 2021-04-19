# Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima 
# y mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van a introducir.
#max = float(input("Ingrese la temperatura maxima del dia: "))
#min = float(input("Ingrese la temperatura minima del dia: "))
def temp_media(maxima, minima):
    return (maxima + minima) / 2
dias = int(input("Ingrese la cantidad de dias:"))
contador = 0
while contador < dias:
    maximo = int(input("Ingrese la temperatura maxima:"))
    minimo = int(input("Ingrese la temperatura minima:"))
    print("Temperatura media:" + " " + str(temp_media(maximo, minimo)) + " " + "grados")
    contador+=1 