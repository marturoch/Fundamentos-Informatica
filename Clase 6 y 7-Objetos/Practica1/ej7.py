#7.Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS 
# (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). 
# El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, 
# por la cantidad total de gramos de comida que ingiere. 
# El CSSP es la misma división pero considerando solamente 
# lo que voló la vez que más voló y lo que comió la vez que más comió. 
# El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. 
# Si un gorrión nunca comió, los coeficientes deben ser None. 
# Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.
class Gorrion:
    def __init__(self, kms, gramos):
        self.kms = kms
        self.gramos = gramos
        self.comidas = []
        self.vuelos = []
    def volar(self, longitud):
        if longitud > 0:
            self.vuelos.append(longitud)
            self.kms += longitud   
    def comer(self, ingerido):
        if ingerido > 0:
            self.comidas.append(ingerido)
            self.gramos += ingerido   
    def CSS(self):
        if self.gramos <= 0:
            return "no puedo devolver el CSS, porque no ha ingerido comida"
        else:
            return self.kms / self.gramos
    def CSSP(self):
        if self.gramos <= 0:
            return "no puedo devolver el CSSP, porque no ha hingerido comida"
        else:
            return int(max(self.vuelos)) / int(max(self.comidas))
    def CSSV(self):
        if len(self.comidas) <= 0:
            return "no puedo devolver el CSSV, porque no ha hingerido comida"
        else:
            return int(len(self.vuelos)/len(self.comidas))

pedro = Gorrion(0,0)
pedro.comer(100) 
pedro.comer(200)
pedro.comer(300) #este es el max
pedro.volar(10)
pedro.volar(20) 
pedro.volar(30) #este es el max
print(pedro.CSS()) #60/600 = 0,1
print(pedro.CSSP()) #30/300 = 0,1
print(pedro.CSSV()) #3/3 = 1