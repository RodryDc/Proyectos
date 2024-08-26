(""")Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar.
En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar
subcondiciones; en su lugar, usar condiciones anidadas.(""")

numero = int(input("Ingresa un numero: ")) #Asignamos el valor a la variable numero

if (numero > 0): #Verificamos si el numero es positivo o negativo
    print("El numero es positivo")
elif (numero < 0):
    print("El numero es negativo")
else:
    print("El numero es 0")

if (numero % 2 == 0): #Verificamos si el numero es par o impar
    print("El numero es par")
else:
    print("El numero es impar")

