num = int(input("Introduce el número del cual quieres hacer el factorial "))

prod = int(1)

while num < 0:
    print("Introduzca un número válido")
    num = int(input("Introduce el número del cual quieres hacer el factorial "))

for i in range(1, (num+1)):
    prod = prod*i

print ("El factorial de tu número es ", prod)

