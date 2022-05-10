#Diseñar una función que calcule el área y el perímetro de una circunferencia. 
#Utiliza dicha función en un programa principal que lea el radio de una 
#circunferencia y muestre su área y perímetro.

 
import math

def surfYperm(radio):
    surf = 0
    perm = 0 
    surf = (radio**2)*(math.pi)
    perm = 2*(math.pi)*radio

    return [surf, perm]

rad = 0
rad = int(input("Introduzca el radio de su circunferencia: "))
print("El área y perímetro de su circunferencia son, respectivamente, ", surfYperm(rad))