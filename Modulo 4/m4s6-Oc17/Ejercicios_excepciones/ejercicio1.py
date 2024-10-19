""" Ejercicio 1: Calculadora de Operaciones Básicas
Crea un programa que permita al usuario ingresar dos números y una operación (suma,
resta, multiplicación, división). El programa debe manejar los casos en los que el
usuario ingresa valores no numéricos o intenta dividir por cero.
Instrucciones:
1. El programa debe solicitar dos números y una operación.
2. Usa try y except para manejar la entrada de datos y posibles errores de
división por cero."""

def calculadora():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")

    try:
        if operacion == "+":
            resultado= num1 + num2
        elif operacion == "-":
            resultado=num1 - num2
        elif operacion == "*":
            resultado=num1 * num2
        elif operacion == "/":
            resultado=num1 / num2
        else:
            raise ValueError("El operador no es valido.")
    except ValueError as err:
        print(f"Error: {err}")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    else:
        print(f"El resultado de la operación es: {resultado}")
    
calculadora()
print("Fin del programa")