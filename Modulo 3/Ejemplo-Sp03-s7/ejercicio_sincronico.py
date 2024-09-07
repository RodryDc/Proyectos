"""Ejercicio de Trabajo en Equipo: Sistema de
Gestión de Inventario de una Tienda
Descripción
Desarrolla un programa que simule la gestión de inventario de una tienda. El programa
debe permitir al usuario realizar las siguientes operaciones:
1. Agregar Productos: Ingresar un nuevo producto al inventario con su nombre,
categoría, cantidad y precio.
2. Buscar Productos: Buscar productos por nombre o categoría, mostrando los
detalles del producto.
3. Actualizar Inventario: Modificar la cantidad de un producto existente (agregar
o reducir stock).
4. Eliminar Productos: Eliminar un producto del inventario.
5. Mostrar Inventario: Mostrar todo el inventario ordenado por nombre, categoría o
precio.
6. Salir: Terminar el programa.
Requisitos Técnicos
Diccionarios: Utiliza un diccionario para almacenar los productos, donde la
clave sea el nombre del producto y el valor sea una tupla con la categoría,
cantidad y precio.
Listas y Tuplas: Usa listas y tuplas para manejar y organizar los datos dentro
del inventario.
Métodos de Strings: Utiliza métodos de cadenas ( str.lower() , str.strip() ,
etc.) para normalizar y validar las entradas del usuario.
Condicionales y Ciclos while : Aplica condicionales para controlar las
operaciones del menú y ciclos while para mantener el programa en ejecución
hasta que el usuario decida salir.
Validación de Entradas: Asegúrate de que los datos ingresados sean válidos (por
ejemplo, cantidades positivas, precios correctos, etc.)."""

#from funciones_menu import agregar_producto,buscar_producto
from os import system
def agregar_producto():
    print("AGREGANDO PRODUCTO")
    nombre = input("Ingresa el nombre del producto: ")
    categoria = input("Ingresa la categoria del producto: ")
    cantidad = int(input("Ingresa la cantidad del producto: "))
    precio = int(input("Ingresa el precio del producto: "))
    inventario[nombre] = (categoria, cantidad, precio)
    print("PRODUCTO AGREGADO CORRECTAMENTE")
    return 

def buscar_producto():
    print("BUSCAR PRODUCTOS")
    while True:
        print("1. Buscar por nombre")
        print("2. Buscar por categoria")
        print("3. Regresar")
        print("----------------------------------------------")
        tipo_busqueda = int(input("\nIngrese una opcion: "))
        if (tipo_busqueda == 1):
            print("BUSCANDO POR NOMBRE")
            nombre = input("Ingresa el nombre del producto: ")
            if nombre in inventario:
                categoria = inventario[nombre][0]
                cantidad = inventario[nombre][1]
                precio = inventario[nombre][2]
                print(f"EL PRODUCTO: {nombre} ES DE CATEGORIA: {categoria}, SU STOCK ES: {cantidad} Y SU VALOR ES: {precio}")
            
        elif (tipo_busqueda == 2):
            print("BUSCANDO POR CATEGORIA")
            categoria = input("Ingresa la categoria del producto: ")
            for clave , valor in inventario.items():
                if categoria in valor:
                    nombre = clave
                    stock = valor[1]
                    precio = valor[2]
                    print(f"EL PRODUCTO: {nombre} ES DE CATEGORIA: {categoria}, SU STOCK ES: {stock} Y SU VALOR ES: {precio}")
                
        elif (tipo_busqueda == 3):
            break 
        else:
            print("Opcion no valida")

        return 

def actualizar_producto():
    print("ACTUALIZAR PRODUCTO")
    actualizar = input("Ingrese el nombre del producto que desea actualizar: ")
    if actualizar in inventario:
        nueva_categoria = input(f"Ingrese la nueva categoria de {actualizar}: ")
        nueva_cantidad = int(input(f"Ingrese la nueva cantidad de {actualizar}: "))        
        while nueva_cantidad < 0:
            print("La cantidad no puede ser negativa")
            nueva_cantidad = int(input(f"Ingrese la nueva cantidad de {actualizar}: "))
        nuevo_precio = int(input(f"Ingrese el nuevo precio de {actualizar}: "))
        while nuevo_precio < 0:
            print("El precio no puede ser negativo")
            nuevo_precio = int(input(f"Ingrese el nuevo precio de {actualizar}: "))  
        inventario[actualizar] = (nueva_categoria, nueva_cantidad, nuevo_precio)
        print("Información actualizada")
    else:
        print("El producto no existe")

def borrar_producto():
    print("BORRAR PRODUCTO")
    print(list(inventario.keys()))
    borrar = input("Ingrese el nombre del producto que desea borrar: ")
    if borrar in inventario:
        del inventario[borrar]
        print("Información eliminada")
    else:
        print("El producto no existe")

def mostrar_inventario():
    print("INVENTARIO")
    for clave , valor in inventario.items():
        print(f"EL PRODUCTO: {clave} ES DE CATEGORIA: {valor[0]}, SU STOCK ES: {valor[1]} Y SU VALOR ES: {valor[2]}")

inventario = {
    "arroz": ("abarrote", 5, 1690),
    "pipeño": ("alcohol", 100, 4990),
    "granadina": ("cocteleria", 100, 5390),
    "helado de piña": ("helados", 200, 4990),
    "leche": ("lacteos", 200, 3990),
    "pisco": ("alcohol", 50, 7990)
}

#Menu
opcion = ""
while opcion != 6:
    print("Bienvenido al Sistema de Gestion de Inventario")
    print("----------------------------------------------")
    print("1. Agregar Productos")
    print("2. Buscar Productos")
    print("3. Actualizar Inventario")
    print("4. Eliminar Productos")
    print("5. Mostrar Inventario")
    print("6. Salir del programa")
    print("----------------------------------------------")

    opcion = int(input("\nIngrese una opcion: "))    

    if (opcion == 1):
        agregar_producto()
    elif (opcion == 2):
        buscar_producto()
    elif (opcion == 3):
        actualizar_producto()
    elif (opcion == 4):
        borrar_producto()
    elif (opcion == 5):
        mostrar_inventario()
    elif (opcion == 6):
        print("SALIR")
        break
    else:
        print("Opcion no valida")

    input("\nPresione una tecla para continuar...")
    system("clear") #limpia la consola