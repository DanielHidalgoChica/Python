#Realizar un programa que lea una cadena por teclado y convierta las 
#mayúsculas a minúsculas y viceversa

cad_or = input("Introduzca la cadena que quiere cambiar: ")
cad_mod = []

for i in cad_or:
    if i.upper() != i:
        cad_mod.append(i.upper())
    else: 
        cad_mod.append(i.lower())

print("Su cadena modificada es: ", end="")
for i in cad_mod:
    print(i, end="")