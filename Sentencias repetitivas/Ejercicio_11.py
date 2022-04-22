#Escribe un programa que diga si un número introducido por teclado es o no 
#primo. Un número primo es aquel que sólo es divisible entre él mismo y la 
#unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si 
#es divisible por algún otro número.
import math

dis = int(0)
num = int(input("Introduzca el número que usted quiere saber si es primo "))
prime = True
flag = True



while flag == True:
    if (num <= 0):
        num = int(input("Introduzca un valor válido para el número "))
    else: flag = False
flag = True

sqrt = math.trunc(num ** 0.5)

for i in range(2, (sqrt+1)):
    if num%i == 0:
        prime = False
        dis = i
        break

if prime == True:
    print("El número que has introducido es primo")
else:
    print("El número que has introducido no es primo, es divisible por ", dis)