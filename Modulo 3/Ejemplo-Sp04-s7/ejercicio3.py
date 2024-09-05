"""Ejercicio 3: Validación de Edad
Descripción
Escribe un programa que pida al usuario ingresar su edad. El programa debe seguir
pidiendo la edad hasta que el usuario ingrese un número válido (entre 18 y 100 años).
Cuando se ingrese un valor válido, el programa debe mostrar un mensaje de
confirmación.
Ejemplo de Ejecución
Ingresa tu edad: 15 Edad no válida. Inténtalo de nuevo. Ingresa tu edad: 120 Edad no
válida. Inténtalo de nuevo. Ingresa tu edad: 25 Edad registrada correctamente."""

edad = int(input("Ingresa tu edad:"))

while (edad < 18) or (edad > 100):
    print("Edad no válida. Inténtalo de nuevo ")
    edad = int(input("Ingresa tu edad:"))

print("Edad registrada correctamente")

