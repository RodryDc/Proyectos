def crear_archivo():
    try:
        archivo = open("ejemplo.txt", "w")
        archivo.write("Hola Mundo")
        archivo.close()
    except FileExistsError as e:
        print("el archivo no se puede crear porque ya existe")
    except Exception as e:
        print("Ha ocurrido un error inesperado")

crear_archivo()

def leer_archivo():
    try:
        archivo = open("ejemplo.txt", "r")
        print(archivo.read())
        archivo.close()
    except FileNotFoundError as e:
        print("el archivo no existe")
    except Exception as e:
        print("Ha ocurrido un error inesperado")

leer_archivo()