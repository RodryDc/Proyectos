#MENU DE NAVEGACION CON WHILE ANIDADO
opcion = ""

while True:
    print("Bienvenido al menu de navegacion")
    print("--------------------------------")
    print("Seleccione una de las siguientes opciones")
    print("1. Inicio de sesión","2. Registrarse", "3. Publicar","4. Salir", sep="\n")

    opcion= int(input("Escriba su opcion: "))

    if (opcion == 1):
        print("Bienvenido al inicio de sesión")
    elif (opcion == 2):
        print("Bienvenido al Registrando")
    elif (opcion == 3):
        print("En este lugar puedes publicar tus ideas")
        
        while True:
            print("Opciones de publicacion")
            print("-----------------------")
            print("Seleccione una de las siguientes opciones")
            print("1. Foto","2. Video", "3. Texto","4. Salir", sep="\n")
            
            sub_opcion= int(input("Escriba su opcion: "))
            
            if (sub_opcion == 1):
                print("Publicaste una foto")
            elif (sub_opcion == 2):
                print("Publicaste un video")
            elif (sub_opcion == 3):
                print("Publicaste un texto")
            elif (sub_opcion == 4):
                print("Saliendo")
                break
            else:
                print("Opcion no valida")
    elif (opcion == 4):
        print("Saliendo")
        break
    else:
        print("Opcion no valida")

print("Ha salido del menu correctamente")