#Crea una función “calcularMaxMin” que recibe una arreglo con valores numérico 
#y devuelve el valor máximo y el mínimo. Crea un programa que pida números 
#por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(muestra):
    aux = muestra[0]
    max = 0 
    min = 0 
    for i in muestra:
        if i > aux:
            aux = i
    max = aux
    for i in muestra:
        if i < aux:
            aux = i
    min = aux
    
    return [max, min]


MaxMin = []

n_day = 0 

n_day = int(input("¿Cuántos números va a introducir? "))

print("Introduzca sus números: ")

for i in range(n_day):
    MaxMin.append(int(input("")))

print("El máximo y el mínimo son: ", calcularMaxMin(MaxMin))

