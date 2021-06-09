#Definí una clase que modele un contador, el cual puede 
# incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual. 
# También puede resetear este valor y al hacerlo se pone en cero. 
# Además es posible indicar directamente un número nuevo que reemplace al valor actual. 
# Este objeto debe entender los siguientes mensajes:
    #inc()
    #dis()
    #reset()
    #valorActual()
    #valorNuevo(nuevoValor)
class Contador:
    def __init__(self, valor): 
        self.valor = valor  #este es el que vamos a ir cambiando
        self.valor_inicial = valor #este es el inicial, no lo cambiamos     
    def inc(self):
        self.valor += 1
    def dis(self):
        self.valor -= 1  
    def reset(self):
        self.valor == 0       
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor        
    def valorActual(self):
        print(self.valor)
    def VolveraValorInicial(self):
        self.valor = self.valor_inicial

#Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 25.
contador = Contador(10) #valor inicial 10
contador.inc() #11
contador.inc() #12
contador.dis() #11
contador.inc() #12
contador.valorActual() #imprime 12
contador.valorNuevo(27)
contador.dis() #26
contador.dis() #25
contador.valorActual() #imprime 25
contador.VolveraValorInicial()
contador.valorActual() #imprime 10, que era el valor inicial