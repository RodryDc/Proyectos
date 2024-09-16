"""Buscar el número más pequeño en una lista
Escribe una función llamada encontrar_menor() que reciba una lista de números y
devuelva el número más pequeño de la lista sin usar la función min() .
Entrada:
encontrar_menor([5, 3, 8, 1, 9])
Salida:
1"""

def encontrar_menor(cadena):
    menor = cadena[0]
    for i in range(len(cadena)):
        if cadena[i] < menor:
            menor = cadena[i]
    return menor

print(encontrar_menor([5, 3, 8, 1, 9]))