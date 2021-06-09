#Desafío VI: Después de tanto programar necesitamos unos matecitos. Hoy aprendiste a prepararlos. 
# Lo que no estoy segura es de que el agua alcance para toda la ronda. 
# Suponiendo que cada cebada de mate consume del 30 ml de agua. 
# Cosntruí una función que nos permita calcular cuántos termos de 1000 ml llenos consumiremos para un ronda dada 
# (es decir una cantidad de personas dada).
def mate(personas):
    agua = (personas * 30)
    resultado = agua / 1000
    if resultado < 1: #si necesito menos de 1l lleno 1 termo
        return 1 
    else:
        if agua%1000 == 0: 
            return int(resultado)
        if agua%1000 != 0:  
            return int(resultado) + 1
print(mate(20)) #menos de 1000ml (600ml en este caso, y necesita 1 termo)
print(mate(100)) #+ de 1000ml y llena termo completo (3000ml, necesita 3 termos)
print(mate(150)) #+ de 1000ml y queda un termo no completo(4500ml, necesita 5 termos y no usa todo el quinto entero)