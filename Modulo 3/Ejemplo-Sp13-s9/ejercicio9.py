"""Calcular la mediana de una lista
Escribe una función llamada calcular_mediana() que reciba una lista de números y
devuelva la mediana. La mediana es el número que está en el medio de una lista
ordenada. Si la lista tiene un número par de elementos, la mediana es el promedio de
los dos números del centro.
Entrada:
calcular_mediana([5, 3, 8, 1, 9])
Salida:
5"""

def calcular_mediana(lista):
    lista.sort()
    if len(lista) % 2 == 0:
        mediana = (lista[len(lista)//2] + lista[len(lista)//2 - 1]) / 2
    else:
        mediana = lista[len(lista)//2]
    return mediana

print(calcular_mediana([5, 3, 8, 1, 9]))