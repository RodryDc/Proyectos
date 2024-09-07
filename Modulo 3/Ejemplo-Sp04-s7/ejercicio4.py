"""Ejercicio 4: Inventario de Productos con Búsqueda
Descripción
Escribe un programa que permita agregar productos a un inventario (nombre del producto
y cantidad). Luego, el usuario debe poder buscar un producto ingresando su nombre y el
programa debe mostrar la cantidad del producto si existe en el inventario, o un
mensaje de "Producto no encontrado" si no existe.
Requisitos
Usa un ciclo while para agregar productos al inventario.
Usa otro ciclo while para permitir la búsqueda de productos hasta que el
usuario decida salir.
Ejemplo de Ejecución
Ingresa el nombre del producto o 'salir' para terminar: manzana Ingresa la cantidad de
manzana: 50 Ingresa el nombre del producto o 'salir' para terminar: naranja Ingresa la
cantidad de naranja: 30 Ingresa el nombre del producto o 'salir' para terminar: salir
Ingresa el nombre del producto que deseas buscar o 'salir' para terminar: manzana La
cantidad de manzana es: 50 Ingresa el nombre del producto que deseas buscar o 'salir'
para terminar: pera Producto no encontrado. Ingresa el nombre del producto que deseas
buscar o 'salir' para terminar: salir"""

inventario = {}
print("Bienvenido al inventario de productos: ")
print("---------------------------------------")

while True:
    nombre = input("\nIngresa el nombre del producto o 'salir' para terminar: ").lower
    if nombre == "salir":
        break
    else:
        cantidad = int(input(f"Ingresa la cantidad de {nombre} : "))
        inventario[nombre] = cantidad
        print(inventario)

while True:
    buscar = input("\nIngresa el nombre del producto que deseas buscar o 'salir' para terminar: ").lower
    if buscar == "salir":
        break
    else:
        if buscar in inventario:
            print(f"La cantidad de {buscar} es: {inventario[buscar]}")
        else:
            print("Producto no encontrado.")