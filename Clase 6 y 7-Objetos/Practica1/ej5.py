#5.Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió
# en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" 
# (para cuando se coloca un valor nuevo). 
# El método para saber el último comando es ultimoComando, y el resultado de aplicarlo a la serie de comandos 
# dicha en el ejercicio anterior debería ser "disminución".
class Contador:
    def __init__(self, valor):
        self.valor = valor 
        self.comando = "" #string vacio   
    def inc(self):
        self.valor += 1
        self.comando = "incremento"
    def dis(self):
        self.valor -= 1
        self.comando = "disminucion"
    def reset(self):
        self.valor == 0
        self.comando = "reset"   
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor
        self.comando = "actualizacion"
    def valorActual(self):
        print(self.valor)
    def ultimoComando(self):
        print(self.comando)

contador = Contador(10) #valor es 10, comando ""
contador.inc() #valor es 11 , comando "incremento"
contador.inc() #valor es 12, comnado "incremento"
contador.dis() #valor es 11, comando "disminucion"
contador.inc() #valor es 12, comando  "incremento"
contador.valorActual() #valor actual es 12, lo imprime
contador.valorNuevo(27) #le damos nuevo valor 27
contador.dis() #valor es 26, comando "disminucion"
contador.dis() #valor es 25, comando "disminucion" 
contador.valorActual() #valor actual es 25, lo imprime
contador.ultimoComando() #el ultimo comando fue disminucion, lo imprime