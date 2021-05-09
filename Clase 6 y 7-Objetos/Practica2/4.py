'''
Ejercicio 4
Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, 
y de estos dos  medios de transporte sabemos que:
=> comienzan con una cantidad que podemos establecer de combustible
=> los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio 
litro de combustible por cada kilómetro recorrido
=> las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;
=> pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible
=> saben responder si entran una cantidad de personas. 
Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera.
'''
class MedioDeTransporte:
    def __init__(self,combustible_en_litros):
        self.combustible_en_litros = combustible_en_litros
        self.personas = []
    def cargar_combustible(self,litros):
        self.combustible_en_litros += litros
    def agregar_pasajeros(self,cantidad_pasajeros):
        if cantidad_pasajeros <= 5 - len(self.personas):
            for _ in range(cantidad_pasajeros):
                self.personas.append(cantidad_pasajeros)
        else:
            return "No puedo agregar mas pasajeros"
class Moto(MedioDeTransporte):
    def recorrer_distancia(self, distancia_en_kms):
        self.combustible_en_litros -= distancia_en_kms * 0,5
class Auto(MedioDeTransporte):
    def recorrer_distancia(self, distancia_en_kms):
        self.combustible_en_litros -= distancia_en_kms
#Pruebo con auto
auto = Auto(40) #40 litros
auto.agregar_pasajeros(2) #agrego 2 pasajeros a la lista
print(len(auto.personas)) #2 
auto.agregar_pasajeros(3) #agrego 3 
print(len(auto.personas)) #5 
print(auto.agregar_pasajeros(1)) #No puede agregar mas porque ya hay 5 y es la capacidad maxima
auto.cargar_combustible(100) #agrego 100 de combustible
print(auto.combustible_en_litros) #40 + 100 = 140
auto.recorrer_distancia(20) #combustible ahora 140 - 20 = 120
print(auto.combustible_en_litros) #120
    