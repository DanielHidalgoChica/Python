#Crea una aplicación que pida un número y calcule su factorial (El factorial de un
#número es el producto de todos los enteros entre 1 y el propio número y se
#representa por el número seguido de un signo de exclamación. Por ejemplo 5! =
#1x2x3x4x5=120)


num = int(input("Introduce el número del cual quieres hacer el factorial "))

prod = int(1)

while num < 0:
    print("Introduzca un número válido")
    num = int(input("Introduce el número del cual quieres hacer el factorial "))

for i in range(1, (num+1)):
    prod = prod*i

print ("El factorial de tu número es ", prod)

