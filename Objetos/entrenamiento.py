#version final 
class EntrenadorDeAves: #puede ir con parentesis tmb EntrenadorDeAves()
    def __init__(self, vacantes):
        self.vacantes = vacantes
        self.alumnos_aceptados = []
    def aceptar(self, alumno):
        if self.vacantes > 0:
            self.alumnos_aceptados.append(alumno)
            self.vacantes -= 1
    def entrenar(self):
        for alumno in self.alumnos_aceptados:
            for _ in range(0, 20):
                alumno.volar_en_circulos()
            alumno.saciar()
    def entrenamiento_intensivo(self):
        for alumno in self.alumnos_aceptados:
            while not alumno.esta_debil: #o is not True
                alumno.volar_en_circulos()
