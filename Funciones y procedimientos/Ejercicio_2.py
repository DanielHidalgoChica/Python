#Crea un programa que pida dos número enteros al usuario y diga si alguno de 
#ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos 
#números, y devuelve si el primero es múltiplo del segundo.


def esMultiplo(x, y):
    if num_2 % num_1 == 0:
        return True
    else:
        return False

num_1 = 0
num_2 = 0
num_1 = int(input("Introduzca su primer número "))
num_2 = int(input("Introduzca el número que quiere comprobar si es múltiplo del primero "))

if esMultiplo(num_1, num_2) == True: print("Es múltiplo")