"""Ejercicio 5: CRUD Básico con Menú
Descripción
Escribe un programa que permita gestionar un inventario de productos mediante un menú
de opciones. El programa debe permitir agregar productos, actualizar la cantidad de
productos, eliminar productos y mostrar todo el inventario. Usa un ciclo while para
permitir que el menú siga activo hasta que el usuario decida salir.
Menú Principal
1. Agregar producto
2. Actualizar cantidad
3. Eliminar producto
4. Mostrar inventario
5. Salir
Requisitos
Usa diccionarios para almacenar los productos y sus cantidades.
Usa menús y ciclos while para permitir la navegación.
Ejemplo de Ejecución
--- Menú ---
Agregar producto Actualizar cantidad Eliminar producto Mostrar inventario Salir
Selecciona una opción: 1 Ingresa el nombre del producto: manzana Ingresa la cantidad
de manzana: 50 Producto agregado.
--- Menú ---
1.Agregar producto 2.Actualizar cantidad 3.Eliminar producto 4.Mostrar inventario
5.Salir Selecciona una opción: 4
Inventario: manzana: 50
--- Menú ---
1.Agregar producto 2.Actualizar cantidad 3.Eliminar producto 4.Mostrar inventario
5.Salir Selecciona una opción: 5 Saliendo del programa..."""

from os import system #limpia la consola

inventario={}

while True:
    print("--- Menú ---")
    print("1.Agregar producto \n2.Actualizar cantidad \n3.Eliminar producto \n4.Mostrar inventario \n5.Salir")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        nombre = input("Ingresa el nombre del producto: ")
        if nombre in inventario:
            print(f"El producto {nombre} ya existe")
        else: 
            cantidad = int(input(f"Ingresa la cantidad de {nombre}: "))
            while cantidad < 0:
                print("La cantidad no puede ser negativa")
                cantidad = int(input(f"Ingresa la cantidad de {nombre}: "))
            inventario[nombre]= cantidad
            print("Producto agregado")
    elif opcion == 2:
        actualizar = input("Ingrese el nombre del producto que desea actualizar: ")
        if actualizar in inventario:
            nueva_cantidad = int(input(f"Ingrese la nueva cantidad de {actualizar}: "))
            while nueva_cantidad < 0:
                print("La cantidad no puede ser negativa")
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad de {actualizar}: "))
            inventario[actualizar] = nueva_cantidad
            print("Cantiad actualizada")
        else:
            print("El producto no existe")
    elif opcion == 3:
        print(list(inventario.keys())) #list() convierte un diccionario en una lista y .keys() obtiene las claves
        borrar = input("Ingrese el nombre del producto que desea borrar: ")
        if borrar in inventario:
            del inventario[borrar]
            print("Producto eliminado")
        else:
            print("El producto no existe")
    elif opcion == 4:
        if not inventario:
            print("Inventario vacío")
        else:
            print("Inventario")
            productos = list(inventario.keys())
            cantidades = list(inventario.values())
            indice = 0
            while indice < len(productos):
                print(f"{productos[indice]} : {cantidades[indice]}")
                indice += 1
        #for clave , valor in inventario.items():            
        #   print(f"{clave} : {valor}")
    elif opcion == 5:
        print("Saliendo del programa")
        break
    else:
        print("Opción No Válida")

    input("Presione una tecla para continuar")
    system("clear") #limpia la consola