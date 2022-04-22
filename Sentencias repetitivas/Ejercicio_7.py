#Realizar una algoritmo que muestre la tabla de multiplicar de un número
#introducido por teclado.

num = int(0)

num = int(input("Introduzca el número del cual quiere ver la tabla de multiplicar: "))

for i in range(0, 11):
    print(num, " x ", i, " = ", num*i)