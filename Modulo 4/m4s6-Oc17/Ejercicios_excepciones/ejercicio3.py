"""Ejercicio 3: Índices en Listas
Dada una lista de colores, crea un programa que permita al usuario ingresar un índice
para acceder a un color en la lista. El programa debe manejar errores cuando el índice
no es válido o está fuera de rango.
Instrucciones:
1. Usa try y except para manejar entradas no válidas y errores de índice.
2. El programa debe continuar solicitando un índice hasta que se ingrese uno
válido."""

colores = ["rojo", "verde", "azul", "amarillo"]

while True:
    try:
        indice = int(input("Ingresa un índice entero entre -4 y 3:"))        
        print(f"Color seleccionado: {colores[indice]}")
    except ValueError:
        print("El valor ingresado debe ser un entero")
    except IndexError:
        print("El índice debe estar entre -4 y 3")
    else:
        break

print("Fin del programa")