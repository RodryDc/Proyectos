"""Filtrar números pares de una lista
Escribe una función llamada filtrar_pares() que reciba una lista de números y
devuelva una nueva lista que contenga solo los números pares.
Entrada:
filtrar_pares([1, 2, 3, 4, 5, 6])
Salida:
[2, 4, 6]"""

def filtrar_pares(cadena):
    pares = []
    for i in range(len(cadena)):
        if cadena[i] % 2 == 0:
            pares.append(cadena[i])
    return pares

print(filtrar_pares([1, 2, 3, 4, 5, 6]))