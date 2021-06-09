#Desafío IX: Modificá la función empanadas_por_gusto() para que devuelva la cantidad de empenadas 
# de cada gusto que deben pedirse a la casa de comidas

pedido = { "Ana" : "no veggie", "Guille" : "no veggie", "Paul" : "veganas", "Luz" : "vegeta", "Marce" : "veganas"}

'''
def empanadas_por_gusto():
    for i in lista_comensales:
        print(pedido[i])
'''
no_veggie = 0
veggie = 0
vegeta = 0 

print(pedido.keys())
print(pedido.values())

nombres = pedido.keys()
for i in pedido:
    if pedido[i] == "no veggie":
        no_veggie = no_veggie + 1
    else:
        if pedido[i] == "veganas":
            veggie = veggie + 1
        else:
            vegeta = vegeta + 1
print("no veggie: " +str(no_veggie))
print("veggie: " +str(veggie))
print("vegeta: " +str(vegeta))