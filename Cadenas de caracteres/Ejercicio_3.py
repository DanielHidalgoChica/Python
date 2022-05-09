#Pide una cadena y un carácter por teclado (valida que sea un carácter) y
#muestra cuantas veces aparece el carácter en la cadena.

string_or = input("Introduce una cadena de caracteres ")
string = string_or.upper()
car_or = input("Introduzca un caracter ")
car = car_or.upper()

if (ord(car) >= 65 and (ord(car) <= 90)):
    print("'", car_or, "'", "es un caracter.")

print("El caracter aparece ", string.count(car), " veces.")
