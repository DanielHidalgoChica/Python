#Suponiendo que hemos introducido una cadena por teclado que representa una 
#frase (palabras separadas por espacios), realiza un programa que cuente 
#cuantas palabras tiene.

cont_esp = 0
frase = input("Introduzca su frase ")

for i in frase:
    if i == " ":
        cont_esp = cont_esp + 1

print("Hay ", (cont_esp + 1), " palabras en la frase.")