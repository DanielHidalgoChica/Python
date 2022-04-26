#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
#sustituye la aparición del primer carácter en la cadena por el segundo carácter.

cad_or = input("Introduzca una cadena de caracteres: ")
cad_mod = []
car_1 = input("Introduzca el caracter que desea sustitutir dentro de esa cadena: ")
car_2 = input("Introduzca el caracter por el que desea sustitutir el anterior: ")

for i in cad_or:
    if i == car_1:
        cad_mod.append(car_2)
    else:
        cad_mod.append(i)

print("Su cadena modificada es: ", end="")
for i in cad_mod:
    print(i, end="")