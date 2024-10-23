"""Diseñe un programa en Python que pida la edad al usuario por consola. El usuario debe ingresar
un número entero; en caso contrario, el programa arrojará una excepción y le solicitará que
ingrese su edad nuevamente.
Seguidamente, el programa debe imprimir que es Adulto si es mayor o igual a 18; y en caso
contrario, no es un adulto"""

while True:
    try:
        edad = int(input("Ingresa tu edad:"))
        if (edad < 18):
            raise ValueError ("No eres mayor de edad")
        print("Eres mayor de edad")
    except ValueError as err:
        print(f"Error: {err}")
    else:
        print(f"La edad ingresada es: {edad}")
        break