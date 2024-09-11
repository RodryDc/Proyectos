"""Filtrar elementos de listas anidadas
Dada una lista de listas, escribe un programa que imprima todos los números mayores
que 10 que se encuentren dentro de las sublistas."""


listas = [[1,12,5], [22,15,3,8], [9,25,2,4], [13,30,10]]

for lista in listas:
    for i in lista:
        if i > 10:
            print(f"{i} es mayor a 10 en la lista {listas.index(lista)}")