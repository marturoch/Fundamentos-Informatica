#desafio IV: Descargá el archivo manipulacion_archivos.txt y creá un programa que lea 
#su contenido y lo imprima en pantalla el resultado de la búsqueda de la expresión -(.*)-
import re 
text = open(r'C:\Users\martu\Documents\martu\UCEMA\2 - PRIMER CUATRI\INFORMATICA\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt', 'r') #aca estamos haciendo que abra el archivo para que lo pueda leer, pero no lo lee todavia
texto = text.read() #lee el archivo
print(texto)
patron = "-(.*)-"
print("\n")
print(re.search(patron, texto).group(1)) #ponemos group1 para que no aparezcan los guiones en el resultado de la busqueda.
text.close()
#Para pensar 🤔: ¿Qué significa dicha expresión regular? Imprimí todo el contenido del archivo y descubrí qué hace este personaje incógnito
    #-(.*)- Busca todas las ocurrencias en el string de los caracteres que no sean un salto de linea y esten entre guiones.
    #En este caso, Elvira Sastre
#Para pensar 🤔: ¿Creés que habrá una forma más práctica de leer archivos estructurados o tabulados?
