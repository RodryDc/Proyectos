"""Almacenar y mostrar información de
estudiantes
Escribe un programa que permita al usuario ingresar el nombre y la calificación de
varios estudiantes. El programa debe almacenar esta información en un diccionario
donde las claves sean los nombres de los estudiantes y los valores sean sus
calificaciones. Al final, el programa debe mostrar el nombre y la calificación de cada
estudiante."""

estudiantes = {}

cantidad = int(input("Ingresa la cantidad de estudiantes que deseas: "))
for i in range(cantidad):
    nombre = input("Ingresa el nombre del estudiante: ")
    calificacion = float(input("Ingresa la calificación del estudiante: "))

    
    estudiantes[nombre] = calificacion

print(estudiantes)

print("\n Otra forma")

while True:
    nombre = input("Ingresa el nombre del estudiante: ")
    if nombre == "":
        break
    calificacion = float(input("Ingresa la calificación del estudiante: "))
    estudiantes[nombre] = calificacion

print(estudiantes)