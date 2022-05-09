#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y 
#devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, 
#“Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use 
#dicha función.

def ConvertirEspaciado(texto):
    text_esp = []
    for i in texto:
        text_esp.append (i + " ")
    return text_esp

txt = input("Introduzca el texto que desea espaciar: ")

print("El texto espaciado es : ", end="")
for i in ConvertirEspaciado(txt):
    print(i, end="")