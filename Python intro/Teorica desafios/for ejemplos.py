lista = [2,3,5,20]
print(lista)
#devolver estos numeros multiplicados x 2 (no a mano)
#para cada elemento de la lista --> "for i in lista"
for i in lista:
    print(i * 2)

pedido = { "Ana" : "no veggie", "Guille" : "no veggie", "Paul" : "veganas", "Luz" : "vegeta", "Marce" : "veganas"}

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
print("no veggie " +str(no_veggie))
print("veggie " +str(veggie))
print("vegeta " +str(vegeta))