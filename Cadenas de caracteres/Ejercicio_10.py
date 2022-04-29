#Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra 
#palíndroma es aquella que se lee igual adelante que atrás

cad_or = input("Introduzca la cadena que quiere comprobar: ")
cad_in = []
cad = []

for i in cad_or:
    cad.append(i)

for i in range(0,len(cad)):
    cad_in.append(cad[len(cad)-i-1])

if (cad_in == cad):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

