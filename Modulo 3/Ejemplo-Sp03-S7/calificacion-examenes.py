#Calificación de exámenes
total_estudiantes = int(input("Ingresa el total de estudiantes: "))
contador=0
acomulador=0

while contador < total_estudiantes:
    nota = float(input(f"Ingresa la nota del estudiante {contador+1}: "))
    acomulador += nota
    print(f"La nota del estudiante {contador+1} es: {nota} y la suma de las notas es: {acomulador}")
    contador += 1

promedio = acomulador / total_estudiantes
print(f"El promedio de las notas es: {promedio:.2f}")



