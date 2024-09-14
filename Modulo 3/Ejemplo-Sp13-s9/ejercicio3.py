"""Escribe una función llamada celsius_a_fahrenheit() que reciba una temperatura en
grados Celsius y la convierta a Fahrenheit.
Entrada:
celsius_a_fahrenheit(25)
Salida:
77.0"""

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(celsius_a_fahrenheit(25))