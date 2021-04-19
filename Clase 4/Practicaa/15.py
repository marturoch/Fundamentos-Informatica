#15.Realizá un programa que validar si una cuenta de mail está escrita correctamente.
import re
mail = "marturoch@gmail.com"
patron = "([a-z,.,A-Z,0-9]{6,30})@(yahoo|hotmail|gmail).com" #lo hice con .com
if re.search(patron, mail) is not None:
    print("Su mail es valido")
else:
    print("su mail es invalido")
