'''
Ejercicio 3
Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un 
=> gorrión (del ejercicio 7 de la práctica anterior), 
=> o Jeuna golondrina. 
Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a 
una rutina que consiste en: 
=> hacerla comer 80 gramos, 
=> hacerla volar 70 kms, y finalmente 
=> hacerla comer otros 10 gramos. Se propone:

implementar la clase Ornitologo, de forma tal que acepte las operaciones 
=> estudiarAve(ave), 
=> avesEnEstudio(), 
=> realizarRutinaSobreAves(), 
=> avesEnEquilibrio(). 
Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. 
Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, 
que responden True cuando se les consulta estaEnEquilibrio().

comprobar el código que se escribió con esta secuencia:

definir un ornitólogo, dos golondrinas y dos gorriones,
inicializar las aves con valores conocidos,
decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
decirle al ornitólogo que realice su rutina sobre aves,
verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.
'''
class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer(self, gramos): #cambiamos comer_alpiste a comer
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):
    return self.energia <= 10

  def saciar(self):
    self.comer_alpiste(100)

  def esta_en_equilibrio(self):
    return self.energia > 150 and self.energia < 300 

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
    def esta_en_equilibrio(self): #hacemos un metodo esta_en_equilibrio para el Gorrion que no tenia
        return self.gramos > 100 and self.gramos < 300 

class Ornitologo:
    def __init__(self):
        self.aves = []
    def estudiarAve(self, ave):
        self.aves.append(ave)
    def avesEnEstudio():
        return self.aves
    def realizarRutinaSobreAves(self):
        for ave in self.aves:
            ave.comer(80)
            ave.volar(70)
            ave.comer(10)
    def avesEnEquilibrio(self,ave):
        return ave.esta_en_equilibrio()

perry = Ornitologo() #inicializamos al ornitologo Perry
julieta = Golondrina(200) #energia 200
print(julieta.energia)
maria = Golondrina(300) #energia 30
jorge = Gorrion(20,30) #kms 20, gramos 30
pedro = Gorrion(10,20) #kms 10, gramos 20 
perry.estudiarAve(julieta)
perry.estudiarAve(jorge)
perry.estudiarAve(pedro)
#a maria no la estudia
print(perry.avesEnEstudio)
perry.realizarRutinaSobreAves()

#JORGE
print(jorge.vuelos) #[70]
print(jorge.comidas) #[80,10]
print(jorge.kms) #10 + 70 = 90 (kms inciales eran 20)
print(jorge.gramos) #30 +80 + 10 = 120(gramos iniciales eran 30)
print(perry.avesEnEquilibrio(jorge))  #TRue porque 120 esta entre 100 y 300

#PEDRO
print(pedro.vuelos) #[70]
print(pedro.comidas) #[80,10]
print(pedro.kms) #10 + 70 = 80 (kms inciales eran 10)
print(pedro.gramos) #20 +80 + 10 = 110(gramos iniciales eran 20)
print(perry.avesEnEquilibrio(pedro)) #True porque 110 esta entre 100 y 300

#JULIETA
#   come 80, sue energia ahora es 200 + (80*4) = 520
#   vuela 70kms, su energia ahora es 520 - (10+70)  = 440 
#   come 10, su energia ahora es 440 + (10*4) = 480
print(julieta.energia) #480
print(perry.avesEnEquilibrio(julieta)) #False porque 480 no esta entre 150 y 300
 
#MARIA
print(maria.energia) #300(misma energia)


