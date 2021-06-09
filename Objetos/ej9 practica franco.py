'''
9. Aflojá con el aparatito
¡Integremos lo visto con otra situación!

Es innegable que en la actualidad los dispositivos electrónicos atraviesan nuestro día a día :electricplug:. Desde celulares :iphone: hasta _notebooks:computer: que están presentes tanto en nuestro ocio como en nuestros trabajos o estudios. Es por eso que vamos a modelar distintos dispositivos utilizando la programación con objetos.

Para entrar en calor vamos a modelar la clase Celular, ¿qué sabemos de ellos?

Todos los celulares tienen su bateria en 100 inicialmente;
Cuando utilizamos un Celular, su batería disminuye en la mitad de los minutos que lo hagamos. Por ejemplo: si usamos el celular 30 minutos, su batería bajará en 15.
Los celulares se pueden cargar_a_tope para dejar la batería en 100.
Definí la clase Celular y también los métodos __init__, utilizar y cargar_a_tope.
No nos vamos a preocupar por ahora en que tenga suficiente bateria para poder utilizarlo. :wink:

¡Ahora es el turno de la Notebook! :computer:

La clase Notebook entiende los mismos mensajes que Celular y se comporta parecido pero no exactamente igual. La diferencia está en que a la hora de utilizar una notebook, su bateria disminuye en la cantidad de minutos que la utilicemos.

Definí la clase Notebook, que sepa entender los mensajes __init__, utilizar y cargar_a_tope.

Sí, definitivamente Celular y Notebook tienen comportamiento repetido. :face_with_raised_eyebrow:

Para pensar: ¿qué métodos son iguales en ambas clases?

Con esto en cuenta, definí una clase abstracta común y modificá las clases que definiste anteriormente para evitar que haya métodos repetidos entre Celular y Notebook. ¿Como la llamarías?

Una de las grandes molestias que nos traen los dispositivos electrónicos es cuando se quedan sin batería. :battery:
Sabemos que tanto los celulares como las notebooks están descargados si tienen 20 o menos de batería. :electric_plug:

Definí el método descargado en donde corresponda.

¿Funciona todo esto que estuvimos haciendo?

Probá en la consola los siguientes comandos:

un_celu = Celular()
una_notebook = Notebook()
un_celu.descargado()
un_celu.utilizar(180)
un_celu.descargado()
una_notebook.utilizar(100)
una_notebook.cargar_a_tope()
una_notebook.descargado()
Ah, pero nos estabamos olvidando de algo fundamental: Lu usa todos los días todos sus dispositivos (con tanta virtualidad no podría ser de otra forma) y necesita recargarlos en su mesita de luz antes de irse a dormir.

Modelá esta situación, para Lu (o cualquier otra persona dueña de aparatitos electrónicos) pueda cargar a tope todos sus dispositivos en un solo comando.

Primero habiamos hecho:
class Celular:
    def __init__(self,bateria):
        self.bateria = 100
    def utilizar(self,minutos):
        self.bateria -= minutos/2
    def cargar_a_tope(self):
        self.bateria = 100
 
 class NoteBook:
    def __init__(self, bateria):
        self.bateria = 100
    def utilizar(self,minutos):
        self.bateria -= minutos
    def cargar_a_tope(self):
        self.bateria = 100
'''
class Dispositivo:
    def __init__(self,bateria):
        self.bateria = 100
    def cargar_a_tope(self):
        self.bateria = 100
    def descargado(self):
        return self.bateria <= 20

class Celular(Dispositivo):
    def utilizar(self,minutos):
        self.bateria -= minutos/2
 
class Notebook(Dispositivo):
    def utilizar(self,minutos):
        self.bateria -= minutos

un_celu = Celular(Dispositivo)
una_notebook = Notebook(Dispositivo)
print(un_celu.descargado()) #como la bateria inicial del celu es 100 y no la modificamos, devuelve false porque no  es <= 20
un_celu.utilizar(180) #la bateria deberia ser 100 - 180/2 = 100 - 90 = 10.
print(un_celu.descargado()) # como la bateria es <= 20, devuelve true
una_notebook.utilizar(100) #la bateria deberia ser 100 - 100 = 0 
una_notebook.cargar_a_tope() #cargamos la bateria a tope, ahora es 100
print(una_notebook.descargado()) #como bateria no es <=20, devuelve false

class duenio: #es un tercero
    def __init__(self): #no le paasamos ningun parametro
        self.dispositivos = [] 
    def agregar(self, dispositivo):
        self.dispositivos.append(dispositivo) #agregamos los dispositivos 
    def cargar(self):
        for i in self.dispositivos: #para cada dispositivo de la lista de dispositivos, los carga a tope
            i.cargar_a_tope()

print(un_celu.bateria)
print(una_notebook.bateria)
lu = duenio()
lu.agregar(un_celu)
lu.agregar(una_notebook)
print(lu.dispositivos)
lu.cargar()
print(un_celu.bateria)
print(una_notebook.bateria)