import random

def francovsGuerra(ite):
    contador_Franco = 0
    contador_Guerra = 0
    for i in range(ite+1):
        if random.randint(0, 1) == 0:
            contador_Franco = contador_Franco + 1
        else:
            contador_Guerra = contador_Guerra + 1
    
    print("Porcentaje Franco: ", contador_Franco*100/(contador_Franco+contador_Guerra))
    print("Porcentaje Guerra: ", contador_Guerra*100/(contador_Franco+contador_Guerra))

    if contador_Guerra == contador_Franco:
        return "Han salido iguales"

    if contador_Franco > contador_Guerra:
        return "Cae Franco"
    else:
        return "Cae Guerra"

ite = int(input("Introduzca el número de iteraciones: "))
    
print(francovsGuerra(ite))




