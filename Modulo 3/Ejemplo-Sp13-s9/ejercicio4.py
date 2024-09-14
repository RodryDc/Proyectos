"""Suma de todos los números de una lista
Escribe una función llamada sumar_lista() que reciba una lista de números y devuelva
la suma de todos los elementos de la lista.
Entrada:
sumar_lista([1, 2, 3, 4, 5])
Salida:
15"""

def sumar_lista(lista):
    sumar = 0
    for numeros in lista:
        sumar += numeros
    return sumar

def sumarlista(lista):
    return sum(lista)

print(sumar_lista([1,2,3,4,5]))    
print(sumarlista([1,2,3,4,5]))    
