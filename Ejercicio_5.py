#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’
#en caso contrario, el programa termina cuando se introduce un espacio.

car = ""

print("Introduce caracteres y te diremos si son vocales o no. Para finalizar el programa introduzca un espacio.")

while car != " ":
    car = str(input("Caracter: "))
    if (car == "a") or (car == "e") or (car == "i") or (car == "o") or (car == "u") or (car == "A") or (car == "E") or (car == "I") or (car == "O") or (car == "U"):
        print("Ha introducido una vocal")
    else: print("No ha introducido una vocal")
    
print("El programa ha finalizado")