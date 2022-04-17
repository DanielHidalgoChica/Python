num = -1
sum = 0
contador = 0 

print("Introduzca los números de los cuales se calculará la suma y la media una vez se intruzca un 0")

while num!=0:
    num = int(input())
    sum = sum + num
    contador = contador + 1

print("La suma de todos estos números es de ", sum, " y su media es de ", sum/contador)