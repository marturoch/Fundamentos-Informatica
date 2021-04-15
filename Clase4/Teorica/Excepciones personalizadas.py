def check_int_type(x):
    if type(x) != int:
        raise TypeError("Only integers are allowed")
#definimos un metodo que chequea si una variable en particular es un entero, y me devuelve un error si no lo es.
check_int_type(4)