#10. Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.
import re
string = "Hola @me&& llamo @@martina@@ y tengo &&19&"
patron = "[@&](.*?)[@&]"
lista = re.findall(patron, string)
print(lista)
for i in lista:
    print(str(i) + str(re.search(i, string).span()))


