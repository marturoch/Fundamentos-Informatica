#7
#def vaquita(costos, comensales):
   # return costos / comensales
#print(vaquita(100,10))

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
print(mate(20)) #menos de 1000ml
print(mate(100)) #+ de 1000ml y llena termo completo
print(mate(150)) #+ de 1000ml y queda un termo no completo