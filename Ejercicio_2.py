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
        


        



    


