#3. Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que
#  recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se 
# aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.
class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def descuento(self, numero):
        descuento = (numero/100) * self.precio
        return (self.precio - descuento) #asi no modificamos el precio, porque solo queremos saber cuanto valdria esa norebook si se aplicase el descuento, pero no lo queremos aplicar
        #si le quisieramos aplicar el descuento:
        #forma 1 self.precio *= 1 - numero/100
        #forma 2 self.precio -= self.precio * *numero/100

mac = Notebook("apple", "air", 1000)
print(mac.marca)
#>>> apple
print(mac.modelo)
#>>> air
print(mac.precio)
#>>> 1000
print(mac.descuento(50))
#>>> 1000 - 500 = 500
print(mac.precio)
#>>> 1000