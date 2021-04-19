def calcular_cantidad_agua(personas):
    litros_tot = (personas * 30)
    resultado = litros_tot / 1000
    if resultado < 1:
        return "Llenar un termo con " + str(litros_tot) + "ml"
    else:
        print("Vas a necesitar mas de un termo")
        if litros_tot%1000 == 0:
            return "Llenar " + str(int(resultado)) + " termos de 1000ml completos"
        else:
            sobrante = litros_tot%1000
            return "Llenar " + str(int(resultado)) + " termos completos y uno con " + str(sobrante) + "ml."
print(calcular_cantidad_agua(20))
print("\n")
print(calcular_cantidad_agua(100))
print("\n")
print(calcular_cantidad_agua(150))

