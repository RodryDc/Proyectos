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

inventario={}

while True:
    print("--- Menú ---")
    print("1.Agregar producto 2.Actualizar cantidad 3.Eliminar producto 4.Mostrar inventario 5.Salir",sep="\n")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        nombre = input("Ingresa el nombre del producto: ")
        cantidad = int(input(f"Ingresa la cantidad de {nombre}:"))
        inventario[nombre]= cantidad
        print("Producto agregado")
    elif opcion == 2:
        actualizar = input("Ingrese el nombre del producto que desea actualizar: ")
        if actualizar in inventario:
            nueva_cantidad = int(input(f"Ingrese la nueva cantidad de {actualizar}: "))
            inventario[actualizar] = nueva_cantidad
            print("Cantiad actualizada")
    elif opcion == 3:
        borrar = input("Ingrese el nombre del producto que desea borrar: ")
        if borrar in inventario:
            del inventario[borrar]
            print("Producto eliminado")
    elif opcion == 4:
        print(f"Inventario: {inventario}")
    elif opcion == 5:
        print("Saliendo del programa")
        break
    else:
        print("Opción No Válida")