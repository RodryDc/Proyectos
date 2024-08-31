#Ejercicio Ag30
#Condiciones
def evaluacion(tipo, categoria, fragil):
    if tipo == "A" and categoria == "Pesado" and fragil == "F":
        msje="Producto alimenticio pesado y frágil: Manejar con extremo cuidado"
    elif tipo == "A" and categoria == "Mediano" and fragil == "F":
        msje="Producto alimenticio mediano y frágil: Manejar con cuidado"
    elif tipo == "A" and categoria == "Ligero":
        msje="Producto alimenticio ligero: Manejar con cuidado estándar"
    elif tipo == "B" and fragil == "F":
        msje="Producto electrónico frágil: Manejar con cuidado"
    elif tipo == "B" and fragil == "N" and categoria == "Pesado":
        msje="Producto electrónico pesado y no frágil: Manejar con precaución"
    elif tipo == "B" and fragil == "N" and categoria == "Mediano" or categoria == "Ligero":
        msje="Producto electrónico no frágil: Manejo estándar"
    elif tipo == "C" and fragil == "F" and categoria == "Pesado":
        msje="Producto pesado y frágil: Manejar con precaución adicional"
    elif tipo == "C" and fragil == "N" and categoria == "Pesado":
        msje="Producto pesado y no frágil: Manejo estándar"
    elif tipo == "C" and categoria == "Mediano" or categoria == "Ligero":
        msje="Producto no pesado: Manejo estándar"
    else:
        print("No existe esa evaluación")

    return print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n",msje,"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def almacen():    
    #Tipo de producto
    tipo = input("\nIngrese el tipo de producto:\n 'A': Producto Alimenticio \n 'B': Productos electrónicos \n 'C': Otros productos \n Opción: ").upper()
    while (tipo != "A" and tipo != "B" and tipo != "C"):
        print("\nTipo de producto no válido")
        tipo = input("\nIngrese el tipo de producto:\n 'A': Producto Alimenticio \n 'B': Productos electrónicos \n 'C': Otros productos \n Opción: ").upper()

    #Peso del producto
    peso = int(input("\nIngrese el peso del producto en (kg): "))
    #Categorización del peso
    if peso >= 20:
        categoria = "Pesado"
    elif peso >= 10:
        categoria = "Mediano"
    else:
        categoria = "Ligero"

    #Fragilidad del producto
    fragil = input("\nIngrese si el producto es frágil:\n'F' (Frágil) \n'N' (No frágil). \n Opción: ").upper()
    while (fragil != "F" and fragil != "N"):
        print("\nTipo de fragilidad no existe")
        fragil = input("\nIngrese si el producto es frágil:\n'F' (Frágil) \n'N' (No frágil). \n Opción: ").upper()

    evaluacion(tipo, categoria, fragil)


print("\nBienvenido al Sistema de Clasificación de Productos del Almacén")
almacen()
continuar = input("\nDesea continuar? (S) = Si \nOpcion: ").upper()
while (continuar == "S"):
    almacen()
    continuar = input("\nDesea continuar? (S) = Si \nOpcion: ").upper()