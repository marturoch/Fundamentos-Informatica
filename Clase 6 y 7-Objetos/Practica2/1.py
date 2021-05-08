'''
Ejercicio 1
Dadas las siguientes clases responder:
- cuales son sus estados
De perro: alimento ; caricias
De gato: alimento ; caricias

- cuales son sus interfaces
De perro: energia, comer, alimento, acariciar, estaDebil, pasear
De gato: energia, comer, caricias, acariciar, estaDebil

- ¿Comparten interfaz?
Comparten: energia, comer, acariciar, estaDebil

- ¿Son polimórficas? 
Polimorficas: comparten parte de la interfaz pero la implementan de forma diferente. 
Y hay una tercera clase que los puede usar indistintamente, les manda un mensaje y ambas 
lo entienden pero lo implementan de distinta manera.
No son polimorficas en este caso porque no hay una tercera clase que las usa indistintamente

OBS:
En perro: alimentos y caricias son atirbutos y metodos => No es un error pero no es recomendable hacer esto
En gato: caricias es atributo y metodo 
'''
class Perro:
    def __init__(self):
        self.alimento = 0 
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

	def alimento(self):
		print(self.alimento)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 2

	def pasear(self, km):
		self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

	def caricias(self):
		print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4