"""Ejercicio 1: Contador de Números Enteros
Descripción
Escribe un programa que pida al usuario ingresar un número entero positivo. El
programa debe mostrar todos los números desde 1 hasta el número ingresado, uno por
uno, utilizando un ciclo while .
Ejemplo de Ejecución
Ingresa un número entero positivo: 5 1 2 3 4 5"""

numero = int(input("Ingresa un número entero y positivo:"))

#while numero < 0:
#    print("El numero debe ser positivo")
#    numero = int(input("Ingresa un número entero y positivo:"))

contador = 1
while contador <= numero:
    print(contador)
    contador +=1