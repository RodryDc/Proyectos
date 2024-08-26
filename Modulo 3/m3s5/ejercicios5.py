(""")Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla.
Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos que hay
entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.(""")

numero = int(input("Ingresa un numero: ")) #Asignamos el valor a la variable numero

factorial = 1
for i in range(1, numero + 1): #Calculamos el factorial
    factorial = factorial * i
print(factorial)
