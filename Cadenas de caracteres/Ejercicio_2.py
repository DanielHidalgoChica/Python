#Realizar un programa que comprueba si una cadena leída por teclado comienza
#por una subcadena introducida por teclado.

cad_prin = input("Introduzca la cadena principal ")
cad_check = input("Introduzca la cadena que quiere comprobar si aparece al principio de la primera ")
cad_aux = ""
contador = 0




while (contador < len(cad_check)):
    if (cad_check[contador] != cad_prin[contador]):
        print("No coinciden")
        exit(0)
    contador = contador + 1
print("Sí coinciden")