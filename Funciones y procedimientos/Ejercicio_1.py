#Crea un procedimiento EscribirCentrado, que reciba como parámetro un texto y 
#lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista: 
#deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el 
#mensaje utilizando el carácter =.
import math
texto = ""

def EscribirCentrado(texto):
    espacios = ""
    for i in range(85-int(math.trunc(len(texto)/2))): 
        espacios = espacios + " "
    print(espacios + texto)

    
texto = str(input("Introduzca el texto que quiere centrar "))


EscribirCentrado(texto)