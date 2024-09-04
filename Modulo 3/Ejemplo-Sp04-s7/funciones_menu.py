from ejercicio_sincronico import inventario

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
            else:
                print("PRODUCTO NO ENCONTRADO")
        elif (tipo_busqueda == 2):
            print("BUSCANDO POR CATEGORIA")
            categoria = input("Ingresa la categoria del producto: ")
            for clave , valor in inventario.items():
                if categoria in valor:
                    nombre = clave
                    stock = valor[1]
                    precio = valor[2]
                    print(f"EL PRODUCTO: {nombre} ES DE CATEGORIA: {categoria}, SU STOCK ES: {stock} Y SU VALOR ES: {precio}")
                else:
                    print("PRODUCTO NO ENCONTRADO")
        elif (tipo_busqueda == 3):
            break 
        else:
            print("Opcion no valida")

        return 