#3. Creá un programa que verifique las siguientes condiciones:
#si un string dado tiene una h seguida de ninguna o más e.
#si un string dado tiene una h seguida de una o más e.
#si un string dado tiene una h seguida de dos o tres e.
import re 
string = input("Ingrese un string:")
patron1 = "(h(e*))"
patron2 = "(h(e+))"
patron3 = "(h(e{2,3}))" #{2,3} implica que haya de 2 a 3, pero puede haber mas de 3 y se sigue cumpliendo porque enocntro el patron.

if re.search(patron1, string) is not None:
    print("El string tiene una h seguida de ninguna o mas e. Se cumple la primer condicion.")
else:
    print("El string no tiene una h seguida de ninguna o mas e. No se cumple la primer condicion.")

if re.search(patron2, string) is not None:
    print("El string tiene una h seguida de una o mas e. Se cumple la segunda condicion.")
else:
    print("El string no tiene una h seguida de una o mas e. No se cumple la segunda condicion.")

if re.search(patron3, string) is not None:
    print("El string tiene una h seguida de dos o tres e. Se cumple la tercer condicion.")
else:
    print("El string no tiene una h seguida de dos o tres e. No se cumple la tercer condicion.")