(""")Crea un archivo main.py en el directorio principal del proyecto.
Importa los módulos gestion y busqueda desde la carpeta contactos .
En el script principal, realiza las siguientes operaciones:
Muestra todos los contactos de la lista lista_contactos .
Permite al usuario agregar un nuevo contacto, solicitando el
nombre y el email.
Muestra nuevamente la lista de contactos actualizada.
Permite al usuario buscar contactos por nombre y muestra los
resultados.(""")

from contactos import gestion, busqueda

def listar_contactos():
    print("Todos los contactos:")
    for contacto in gestion.lista_contactos:
        print(f"Nombre: {contacto[0]}, Email: {contacto[1]}")


def nuevo_contacto():
    nombre = input("Ingresa el nombre del contacto que deseas agregar: ")
    email = input("Ingresa el email del contacto que deseas agregar: ")
    gestion.agregar_contacto(nombre, email)
    print(f"Contacto {nombre} agregado exitosamente")

def buscar_contacto():
    nombre = input("Ingresa el nombre del contacto que deseas buscar: ")
    contactos_encontrados = busqueda.buscar_contacto(nombre)
    for contacto in contactos_encontrados:
        print(f"Nombre: {contacto[0]}, Email: {contacto[1]}")


listar_contactos()
nuevo_contacto()
print("Contactos actualizados:")
listar_contactos()


print("SELECCIONA UNA OPCION: \n1. Listar contactos \n2. Agregar contacto \n3. Buscar contacto \n4. Salir")
opcion = int(input())

while (opcion != 4):
    if (opcion == 1):
        listar_contactos()
    elif (opcion == 2):
        nuevo_contacto()
    elif (opcion == 3):
        buscar_contacto()
    else:
        print("Opcion no valida")
    print("SELECCIONA UNA OPCION: \n1. Listar contactos \n2. Agregar contacto \n3. Buscar contacto \n4. Salir")
    opcion = int(input())
