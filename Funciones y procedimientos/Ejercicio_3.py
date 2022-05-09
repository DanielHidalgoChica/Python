#Crear una función que calcule la temperatura media de un día a partir de la 
#temperatura máxima y mínima. Crear un programa principal, que utilizando la 
#función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y 
#vaya mostrando la media. El programa pedirá el número de días que se van a 
#introducir.

def avgDay(x, y):
    return (x + y)/2

n_days = int(input("¿Cuántos días vas a introducir? "))

for i in range(n_days):
    temp_max = int(input("Temperatura máxima: "))
    temp_min = int(input("Temperatura mínima: "))

    print("La temperatura media es: ", avgDay(temp_max, temp_min))
