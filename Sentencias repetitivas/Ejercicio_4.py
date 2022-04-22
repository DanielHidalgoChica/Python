#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
#números a introducir). El programa debe informar de cuantos números
#introducidos son mayores que 0, menores que 0 e iguales a 0.
times = int(-1)
ov_zero = int(0)
un_zero = int(0)
eq_zero = int(0)

times = int(input("¿Cuántos números va a querer introducir? "))
while times <= 0:
    print("Introduzca un valor coherente de veces")
    times = int(input("¿Cuántos números va a querer introducir? "))


print("Introduzca los números")
for i in range (0,times):
    num = int(input())
    if num == 0:
        eq_zero = eq_zero + 1
    else:
        if num > 0: 
            ov_zero = ov_zero + 1
        else: un_zero = un_zero + 1
print("Número de zeros introducidos: ", eq_zero)
print("Número de números mayores a zero introducidos: ", ov_zero)
print("Número de números menores que zero introducidos: ", un_zero)