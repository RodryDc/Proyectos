"""Calcular el promedio de una lista de calificaciones
Escribe una función llamada calcular_promedio() que reciba una lista de
calificaciones y devuelva el promedio de estas.
Entrada:
calcular_promedio([80, 90, 85, 70, 95])
Salida:
84.0"""

def calcular_promedio(calificaciones):
    suma = 0
    for notas in calificaciones:
        suma += notas
    promedio = suma / len(calificaciones)
    return promedio

print(calcular_promedio([80,90,85,70,95]))
