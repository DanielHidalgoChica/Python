#Escribe un programa que pida el limite inferior y superior de un intervalo. Si el
#límite inferior es mayor que el superior lo tiene que volver a pedir.
#A continuación se van introduciendo números hasta que introduzcamos el 0.
#Cuando termine el programa dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# Informa si hemos introducido algún número igual a los límites del intervalo.

nums = int(-1)
vDentro = []
vFuera = []
eq_limits = False
suma = int(0)


flag = False
while flag == False:
    try:
        lim_sup = int(input("Introduzca el límite superior de su intervalo "))
        lim_inf = int(input("Introduzca el límite inferior de su intervalo "))
        flag = True
    except:
        print("Introduzca unos valores válidos para los límites ")
flag = False

while lim_sup <= lim_inf:
    print("Introduzca unos valores válidos para los límites ")
    lim_sup = int(input("Introduzca el límite superior de su intervalo "))
    lim_inf = int(input("Introduzca el límite inferior de su intervalo "))

print("Introduzca los números (cuando termine introduzca un zero) ")

while nums != 0:
    flag = False
    while flag == False:
        try:
            nums = int(input())
            flag = True
        except:
            print("Introduzca unos valores válidos para los números ")

    if nums == 0: break
    if nums < lim_inf or nums > lim_sup:
        vFuera.append(nums)
    else: 
        vDentro.append(nums)
    if nums == lim_inf or nums == lim_sup:
        eq_limits = True

for i in vDentro:
    suma = suma +  i 

print("La suma de los números dentro del intervalo es de ", suma)

print("Fuera del intervalo había ", len(vFuera), "números")

if eq_limits == True:
    print("Ha introducido algún número igual a los límites del intervalo")
else:
    print("No ha introducido ningún número igual a los límites del intervalo")
