
def printMenu():
    print("1- Ejercicio 1 ")
    print("2- Ejercicio 2 ")
    print("3- Salir ")
    

def seleccionOpcion():
    printMenu()
    opt = 0 
    while (opt < 1 or opt > 3):
     opt = (int) (input("Seleccione una opción: "))
    return opt

opc = 0 
while (opc != 3):
    opc = seleccionOpcion()
    match opc:
        case 1:
            print("Ejercicio 1")
        case 2:
            print("Ejercicio 2")
        case 3:
            print("ByeBye")
