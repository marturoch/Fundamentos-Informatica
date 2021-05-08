#Ejercicio 1
#Dada la siguiente clase, identificá la interfaz y el estado de la misma:
#Interfaz: Lista de metodos que tiene el objeto. Mensajes que entiende un objeto.Les mandamos mensajes a los objetos para que hagan algo. Nombre de objeto.mensaje.
#Estado: Lista de atributos que tiene un objeto. Estos atributos estan definidos en el constructor def __init__(self)
class Perro:
    def __init__(self): #no le pasamos ningun argumento extra en este caso. Si le paso argumentos
        self._alimento = 0 #alimento inciializado con un valor inicial. Este valor puede estar efinido como en este caso o puede estar dado por el usuario
        self._caricias = 0
#El estado es alimento y caricias
#La interfaz es energia, comer, acariciar y estaDebil
def __init__ (self, cantidad_de_alimentos, cantidad_de_caricias):
    self.cantidad_de_alimentos
    self cantidad_de_caricias

    def energia(self): 
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

josefa = Golondrina(2)