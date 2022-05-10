#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una 
#contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la 
#contraseña es “asdasd”. Además recibe el número de intentos que se ha 
#intentado hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una 
#contraseña y se intente hacer login, solamente tenemos tres oportunidades para 
#intentarlo.

def Login(username, psswd):
    if username == "usuario1" and psswd == "asdasd":
        return True
    else: return False

intentos = 0 

while intentos < 3:
    usuario = str(input("Introduzca el nombre de usuario: "))
    contraseña = str(input("Introduzca la contraseña: "))

    if Login(usuario, contraseña) == True:
        print("Inicion de sesión exitoso.")
        exit()
    else: 
        print("Usuario o contraseña incorrectos.")
        intentos = intentos + 1

print("Se han terminado los intentos disponibles.")


