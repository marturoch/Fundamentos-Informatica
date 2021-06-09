#Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. 
# Este objeto debe entender los siguientes mensajes:
    #cargar(numero)
    #sumar(numero)
    #restar(numero)
    #multiplicar(numero)
    #valorActual()

class Calculadora:
    def __init__(self, numero = 0): #porque asumimos que arranca en 0 la calcu y no hay que pasarle ningun parametro cuando queremos inciializar el objeto
        self.numero = numero
    #si hubiesemos hecho:
    #def __init__(self, numero):
    #   self.numero = 0 --> estamos hacieno que el atributo siempre sea 0, mas alla del valor que le paso como parametro cuando inicializo al objeto. Pero hay que pasarle un parametro.
    def cargar(self, numero):
        self.numero += numero   
    def sumar(self, numero):
        self.numero += numero
    def restar(self, numero):
        self.numero -= numero   
    def multiplicar(self, numero):
        self.numero *= numero    
    def valorActual(self):
        print(self.numero)
        
# Si se evalúa la siguiente secuencia:
calculadora = Calculadora() #numero = 0 porque lo pusimos por parametro
calculadora.cargar(0) #numero = 0
calculadora.sumar(4) #numero = 0 + 4 = 4
calculadora.multiplicar(5) #numero = 4 * 5 = 20
calculadora.restar(8) #numero = 20 - 8 = 12 
calculadora.multiplicar(2) #numero = 12 * 2 = 24
calculadora.valorActual() # 24
# el resultado debe ser 24.