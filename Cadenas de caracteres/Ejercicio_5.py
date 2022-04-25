#Si tenemos una cadena con un nombre y apellidos, realizar un programa que 
#muestre las iniciales en mayúsculas.

nombre_c = input("Introduzca su nombre y sus apellidos ")
if nombre_c.count(" ") == 2:
    print(nombre_c[0].upper(), ".", nombre_c[nombre_c.index(" ")+1].upper())
else:
    print(nombre_c[0].upper(), ".", nombre_c[nombre_c.index(" ")+1].upper(), ".", nombre_c[nombre_c.index(" ", nombre_c.index(" ")+1)+1].upper())
    
