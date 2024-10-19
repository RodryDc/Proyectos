"""Ejercicio 2: Validación de Edad
Escribe un programa que solicite al usuario ingresar su edad. El programa debe
verificar que el usuario ingrese un número entero válido y que este número sea
positivo.
Instrucciones:
1. Usa try y except para manejar entradas no válidas.
2. Si la edad ingresada no es válida o es menor que 0, el programa debe imprimir
un mensaje de error."""


while True:
    try:
        edad = int(input("Ingresa tu edad:"))
        if (edad < 0):
            raise ValueError ("Edad no puede ser negativa")
        print("Edad registrada correctamente")
    except ValueError as err:
        print(f"Error: {err}")
    else:
        print(f"La edad ingresada es: {edad}")
        break
    
print("Fin del programa")