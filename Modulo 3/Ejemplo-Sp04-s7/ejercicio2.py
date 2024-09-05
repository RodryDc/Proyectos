"""Ejercicio 2: Suma de Números Pares
Descripción
Escribe un programa que pida al usuario ingresar un número entero positivo. El
programa debe sumar todos los números pares desde 1 hasta el número ingresado y
mostrar el resultado.
Ejemplo de Ejecución
Ingresa un número entero positivo: 6 La suma de los números pares es: 12"""

numero = int(input("Ingresa un número entero y positivo:"))

contador = 1
suma = 0
while contador <= numero:
    if contador % 2 == 0:
        print(contador)
        suma = suma + contador
    contador += 1

print(f"La suma de los números pares es: {suma}")