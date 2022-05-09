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

print("Introduzca sus números: ")

print("El máximo y el mínimo son: " calcularMaxMin())