#Realizar un programa que compruebe si una cadena contiene una subcadena. 
#Las dos cadenas se introducen por teclado

cad_prin = input("Introduzca la cadena principal: ")
cad_check_or = input("Introduzca la subcadena que quiere comprobar si se encuentra en la principal: ")
cad_check = []
cad_aux = []
eq = False

for i in cad_check_or:
    cad_check.append(i)

for i in range(0, len(cad_prin)):
    cad_aux = []
    if cad_prin[i] == cad_check[0]:
        for j in range(i, i+len(cad_check)):
            cad_aux.append(cad_prin[j])

    if cad_aux == cad_check:
        eq = True
        break

if eq == True:
    print("La subcadena se encuentra dentro de la cadena")
else: print("La subcadena no se encuentra dentro de la cadena")