
guess = 0
import random

num = int(random.randint(10, 20))

print(num)

while guess != num:
    guess = int(input("Adivina el número "))
    if guess<num:
        print("El número es mayor")
    else:
        print("El número es menor")

print("Has acertado el número!")