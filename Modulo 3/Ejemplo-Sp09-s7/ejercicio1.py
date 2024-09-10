"""IMprimir los numeros pares entre 1 y 20"""
print("Imprimir los numeros pares entre 1 y 20")
print("\nprimera forma")
for i in range(21):
    if i % 2 == 0:
        print(f"{i} es par")

print("\nsegunda forma")
for i in range(1,21):
    if i % 2 == 0:
        print(f"{i} es par")

print("\ntercera forma")
for i in range(2,21,2):
    print(f"{i} es par")


"""Imprimir las tablas dado un numero ingresado por el usuario"""

print("\nImprimir las tablas dado un numero")
numero = int(input("Ingresa un numero: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

"""sumar los elementos de una lista"""

print("\nSumar los elementos de una lista")
numero = int(input("Ingresa la cantidad de elementos: "))
lista = []
for i in range(numero):
    elemento = int(input(f"Ingresa el elemento {i+1}: "))
    lista.append(elemento)
suma = 0
for i in lista:
    suma += i
print(f"la suma es: {suma}")

print("\n Otro ejemplo ")
lista=[2,5,63,8,8,5]
suma = 0
for numero in lista:
    suma += numero

print(f"La suma de la lista es {suma}")

print("\n Otro ejemplo pero con len")
lista=[2,5,63,8,8,5]
suma = 0
for numero in range(len(lista)):
    suma += lista[numero]

print(f"La suma de la lista es {suma}")

"""rescatar el numero mayor de una lista"""

print("\nRescatar el numero mayor de una lista")
lista = [2,5,63,8,8,5,53,22,64,80]
mayor = 0
for numero in lista:
    if numero > mayor:
        mayor = numero
print(f"El numero mayor de la lista es {mayor}")