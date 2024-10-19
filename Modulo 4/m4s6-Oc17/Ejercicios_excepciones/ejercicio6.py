"""Ejercicio 6: Raíces Cuadradas de una Lista
Crea un programa que solicite al usuario ingresar una lista de números separados por
comas y calcule la raíz cuadrada de cada número. El programa debe manejar entradas no
válidas y también debe manejar números negativos (dado que no se puede calcular la
raíz cuadrada de un número negativo sin complejos).
Instrucciones:
1. Usa try y except para manejar números no válidos o negativos.
2. Si el usuario ingresa un número negativo, se debe imprimir un mensaje de error."""

from math import sqrt
while True:
    try:
        lista_numeros = input("INgrese una lista de numeros separados por comas (,)\n")
        for numero in lista_numeros.split(","):
            if numero < 0:
                raise ValueError("No se puede calcular la reiz de un numero negativo")
        print(f"La raiz cuadrada de {numero} es {sqrt(numero)}")
    except ValueError as err:
        print(f"Error: {err}")
    else:
        break

print("Fin del codigo")

        