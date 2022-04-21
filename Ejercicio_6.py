#Escribir un programa que imprima todos los números pares entre dos números
#que se le pidan al usuario.

lim_inf = 0
lim_sup = 0
flag = True

while flag == True:
    try: 
        lim_inf = int(input("¿Desde qué número quiere que se le digan los números pares? "))
        flag = False
    except: 
        print("Introduzca un valor válido")
        

flag = True

while flag == True:
    try: 
        lim_sup = int(input("¿Hasta qué número quiere que se le digan los números pares? "))
        flag = False
    except: 
        print("Introduzca un valor válido")
        



for i in range (lim_inf, (lim_sup+1)):
    if i%2 == 0:
        print (i)
