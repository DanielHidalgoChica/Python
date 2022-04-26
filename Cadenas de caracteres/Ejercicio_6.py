#Realizar un programa que dada una cadena de caracteres por caracteres, 
#genere otra cadena resultado de invertir la primera.

cad = input("Introduzca la cadena que desea invertir: ")
cad_in = []

for i in range(len(cad)):
    cad_in.append(cad[(len(cad)-1)-i])

print("La cadne invertida es: ", end="")
for i in cad_in:
    print(i, end="")
