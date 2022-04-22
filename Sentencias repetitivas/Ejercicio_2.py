#Crea una aplicación que permita adivinar un número. La aplicación genera un
#número aleatorio del 1 al 100. A continuación va pidiendo números y va
#respondiendo si el número a adivinar es mayor o menor que el introducido,a
#demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El
#programa termina cuando se acierta el número (además te dice en cuantos
#intentos lo has acertado), si se llega al limite de intentos te muestra el número
#que había generado.


intentos_res = 10
guess = 0

import random
num = int(random.randint(1, 100))

guess = int(input("Adivina el número "))

if guess==num:
    print("Has acertado el número a la primera")
else:
    while (guess != num):
        intentos_res = intentos_res - 1
        if intentos_res == 0:
            break
        else:
            if guess<num:
                print("El número es mayor")
                print("Te quedan ", intentos_res, "intentos")
                guess = int(input("Adivina el número "))
            else:
                print("El número es menor")
                print("Te quedan ", intentos_res, "intentos")
                guess = int(input("Adivina el número "))
    if guess == num:
        print("Has acertado el número en ", 10-intentos_res+1, " intentos")
    else:
        print("Lo siento, no lo has conseguido. El número que buscabas era el ", num) 
        


        



    


