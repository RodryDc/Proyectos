print("\n con 1 elemento")
for i in range(7): #range es una lista de 7 elementos del 0 al 6
    print(f" iteracion{i}")

print("\n con 2 elementos")
for i in range(2, 7): #range es una lista de 5 elementos del 2 al 6
    print(f" iteracion{i}")

print("\n con 3 elementos")
for i in range(2, 10, 2): #range es una lista de 5 elementos del 2 al 10, de dos en dos 
    print(f" iteracion{i}")

print("\n Ejemplo par o impar")
for i in range(10):
    if i % 2 == 0:
        print(f"el número {i} es par")
    else:
        print(f"el número {i} es impar")
        
print("\n Ejemplo listas")
productos = [
    ("manzana", 1.0),
    ("pera", 1.5),
    ("naranja", 2.0)
]

print("\nRecorriendo una lista de tuplas")
for producto, precio in productos: #recorremos la lista de tuplas con dos elementos
    print(f"El producto {producto}, tiene un valor de ${precio}")

frutas =["manzana", "pera", "naranja"]
for fruta in frutas:
    print(f"La fruta es: {fruta}")

print(list(enumerate(frutas))) #devuelve una lista de tuplas (indice, valor)

frutas =["manzana", "pera", "naranja"]
for i, fruta in enumerate(frutas):
    print(f"En el indice {i} La fruta es: {fruta}")


print("\n Ejemplo listas con enumerate")
productos_emumerate = [
    ("manzana", 1.0),
    ("pera", 1.5),
    ("naranja", 2.0)
]

print("\nRecorriendo una lista de tuplas")
for i,producto in enumerate(productos_emumerate): 
    print(f"El producto {producto}, tiene un valor de ${productos_emumerate[i][1]}, ambos en el indice {i}")

print("\nEJEMPLO LISTAS CON ENUMERATE Y SIN ENUMERATE")
lista_original =[
    "elemento 1",
    "elemento 2",
    "elemento 3"
]

lista_enumerate =[
    (0, "elemento 1"),
    (1, "elemento 2"),
    (2, "elemento 3")
]

print("\nRecorriendo una lista sin enumerate")
for i,elemento in lista_enumerate:
    print(f"El elemento {i} es: {elemento}")

print("\nRecorriendo una lista con enumerate")
for i,elemento in enumerate(lista_original):
    print(f"El elemento {i} es: {elemento}")

print("\nRecorriendo una lista con enumerate con acceso al elemento")
for i,elemento in enumerate(lista_enumerate):
    print(f"El elemento {i} es: {elemento[1]}")


# EXPLICACION DE COMO SE ACCEDE A LOS ELEMENTOS DE UNA TUPLA
# tupla_externa = (4, ("manzana",1.0, ("elemento a", "elemento b")))
# tupla_interna = ("manzana",1.0, ("elemento a", "elemento b"))
 
# tupla_externa[0] -> 4
# tupla_externa[1] = tupla_interna
 
# tupla_externa[1][1]-> 1.0
# tupla_externa[1][2][0] -> "elemento a"

productos= [
    ("manzana", 1.0),
    ("pera", 1.5),
    ("naranja", 2.0)
]

print("\nRecorriendo una lista con los indices de una tupla")
for tupla_enumerate in enumerate(productos): 
    print(f"El producto {tupla_enumerate[1][0]}, tiene un valor de ${productos_emumerate[1][1]}, ambos en el indice {tupla_enumerate[0]}")


