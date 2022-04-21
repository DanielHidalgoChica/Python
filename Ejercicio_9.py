#Escribe un programa que dados dos números, uno real (base) y un entero 
#positivo (exponente), saque por pantalla el resultado de la potencia. No se puede 
#utilizar el operador de potencia.

base = int(0)
exp = int(0)
answ = int(1)



base = int(input("Introduzca la base de la potencia "))
exp = int(input("Introduzca el exponente de la potencia "))

if exp == 0: 
    answ = 1
else:
    if exp > 0:
        for i in range (1, (exp+1)):
            answ = base * answ
    else: 
        for i in range (1, ((-exp)+1)):
            answ = base * answ
        answ = 1/answ


print("El resultado de su potencia es ", answ)
