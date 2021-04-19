#11. Realizá un programa que dado una lista de strings verifique que dos 
# palabras dentro del string empiecen con la letra P y las imprima. 
#(Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
import re
#Como lo hice yo 
lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
for i in lista:
    patron = "(P\w*)"
    strings = re.findall(patron, i) 
    if len(strings) == 2:
        print(strings[0] + " " + (strings[1]))
'''
Como lo hizo Guille:
listaa = ["hola Práctica sjndeui Python", "Práctica C++", "Práctica Fortran"]
def dos_P(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)",elemento)
        if resultado is not None:
            print(resultado.group())
dos_P(listaa)
'''