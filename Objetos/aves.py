valparaiso = 4533
buenos_aires = 3078
ushuaia = 0

class Ave: # clase abstracta
  def esta_feliz(self):
    return self.energia > 500

  def arranca_en(self, ciudad):
    self.ciudad_actual = ciudad #se puede poner un atributo directamente en un metodo, en este caso ciudad_actual

  def volar_por_panamericana(self, ciudad_destino):
    kms = abs(self.ciudad_actual - ciudad_destino)
    self.volar(kms)
    self.ciudad_actual = ciudad_destino
    #volar por panamericana define / envia un mensaje que no esta definido en Ave ("volar") y esta en las clases fijas

class Golondrina(Ave): # Golondrina hereda de Ave
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia = self.energia + 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):
    return self.energia <= 10

  def saciar(self):
    self.comer_alpiste(100)

class Dragon(Ave): # Dragon hereda de Ave
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def saciar(self):
    self.comer_peces(3)

  def esta_debil(self):
    return self.energia < 50

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
chimuelo = Dragon(200, 1000)

valparaiso = 4533
buenos_aires = 3078
ushuaia = 0

chimuelo.arranca_en(ushuaia)
print(chimuelo.ciudad_actual) #ushuaia , es decir 0
chimuelo.volar_por_panamericana(buenos_aires)
#(0 - 3078) = -3078 => devuelve el absoluto, 3078
#pepita.volar(3078):
# self.energia -= 10 + 3078/10 
#self.energia -= 317,8
#self.energia = 1000 - 317,8 = 1012
print(chimuelo.energia) #682,2
print(chimuelo.ciudad_actual) #buenos_aires, es decir 3078