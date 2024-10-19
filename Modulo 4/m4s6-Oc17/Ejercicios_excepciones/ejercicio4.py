"""Ejercicio 4: Conversión de Temperaturas
Crea un programa que convierta temperaturas de grados Celsius a Fahrenheit. El
programa debe asegurarse de que el usuario ingrese un número válido para la
temperatura en Celsius.
Instrucciones:
1. Usa try y except para manejar entradas no válidas.
2. Si el usuario ingresa un valor no numérico, el programa debe solicitar la
entrada de nuevo."""

while True:
    try:
        celsius = float(input("Ingrese la temperatura en °C: "))
        farenheit = (celsius *9/5) + 32
        print(f"La temperatura en °F es: {farenheit}")
    except ValueError:
        print("Error: Debes ingresar una temperatura valida ")
    else:
        break

print("Fin del programa") 