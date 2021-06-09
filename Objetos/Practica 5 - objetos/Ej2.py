#2. Modificá el método volar de la clase Golondrina visto en la clase de teoría 
# de manera que no pueda volar si al hacerlo la energía toma el valor 0 
# o valor negativo.
class Golondrina:
  def __init__(self, energia):
    self.energia = energia
  def comer_alpiste(self, gramos): 
    self.energia += 4 * gramos 
  def volar_en_circulos(self): 
    self.volar(0) 
  def volar(self, kms):
    if (10 + kms < self.energia):
          self.energia -= 10 + kms
    else:
        print("No puedo volar esa distancia, no tengo suficiente energia, necesito comer")      
  def esta_debil(self): 
    return self.energia <= 10
  def esta_feliz(self):
        return self.energia > 500

pepita = Golondrina(100) #energia inicial 100
pepita.volar(9) #10 + 9 = 19 --> 19 es menor a 100 que es su energia, entonces puede volar y perder 19 de energia
print(pepita.energia) #81 ahora tiene 100 - 19 = 81 de energia
pepita.volar(100) #100 + 10 = 110 es mayor a 81, no puede volar