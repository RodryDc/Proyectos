"""Sumar números variables con *args
Escribe una función llamada sumar_numeros() que acepte una cantidad variable de
números utilizando *args y devuelva la suma de todos ellos.
Entrada:
sumar_numeros(5, 10, 15, 20)
Salida:
50"""

def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(5,10,15,20))


def presentacion(nombre, *colores):
    print(f"Hola, mi nombre es {nombre} y mis colores favoritos son: {colores}")

print("\n Otro ejemplo:")
presentacion("Juan", "rojo", "azul", "verde")