#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la
#suma y la media de todos los números introducidos.

num = int(-1)
sum = int(0)
contador = int(0) 

print("Introduzca los números de los cuales se calculará la suma y la media una vez se intruzca un 0")

while num!=0:
    num = int(input())
    sum = sum + num
    contador = contador + 1

print("La suma de todos estos números es de ", sum, " y su media es de ", sum/contador)