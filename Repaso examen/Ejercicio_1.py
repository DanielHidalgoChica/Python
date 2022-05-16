#Meter números aleatorios en una lista
#Pasados 10s, mostrar los elementos

import random
import time

def añadirNum(num_ent):
    contador = 0 
    contador = num_ent
    vNumeros = []
    for i in range(1, contador+1):
        vNumeros.append(random.randint(0,10))
        time.sleep(0.5)
    return (vNumeros)

flag = True
while flag == True:   
    try:     
        num = int(input("¿Cuántos números quieres que se añadan? "))
        flag = False
    except: 
        print("Introduce un valor válido")


print (añadirNum(num))