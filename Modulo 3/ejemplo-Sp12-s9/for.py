colores = ["azul","amarillo","rojo", "negro"]
frutas = ["manzana", "pera", "naranja"]

# for color in colores:
#     print(color)

# for fruta in frutas:
#     print(fruta)

# def imprimir_elementos(lista):
#     for elemento in lista:
#         print(elemento)

# imprimir_elementos(frutas)
# imprimir_elementos(colores)

def imprimir_elementos2(*args):
    for elemento in args:
        print(elemento)

imprimir_elementos2(frutas, colores)
