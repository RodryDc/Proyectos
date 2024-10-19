"""Ejercicio 5: Cálculo de Promedio
Escribe un programa que solicite al usuario ingresar una lista de números separados
por comas y luego calcule el promedio. El programa debe manejar entradas no válidas.
Instrucciones:
1. Usa try y except para manejar errores si el usuario no ingresa números
válidos.
2. El programa debe seguir solicitando la lista hasta que el usuario ingrese
números correctamente."""


while True:
    try:
        lista_notas = input("ingresa las nota separadas por comas (,):\n")
        numeros = []
        for numero in lista_notas.split(","):
            numeros.append(float(numero))
        
        promedio = sum(numeros)/len(numeros)
        print(f"EL promedio de las notas entregadas es {promedio}")
    except ValueError:
        print("El formato de la lista no es correcto")
    else:
        break

print("Fin del codigo")