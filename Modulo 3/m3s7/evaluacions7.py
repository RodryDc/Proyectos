(""")Dada una lista de diccionarios que representan información de estudiantes, realiza las siguientes
tareas:
estudiantes = [
 {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
 {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
 {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
 {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
 {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]
Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Filtra y muestra únicamente los estudiantes que tienen más de 18 años y cuyo promedio de
calificaciones sea superior a 85.
• Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 años y
cuya edad sea un número primo.(""")


estudiantes = [
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

for estudiante in estudiantes:
    if estudiante['edad'] > 18:
        promedio = sum(estudiante['calificaciones']) / len(estudiante['calificaciones'])
        if promedio > 85:
            print(estudiante, "con promedio:", promedio)
  
def es_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

promedio = 0
contador = 0
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and es_primo(estudiante['edad']):
        print(estudiante)
        promedio += sum(estudiante['calificaciones']) / len(estudiante['calificaciones'])
        contador += 1
        
print("El promedio de las calificaciones de los estudiantes mayores de 18 y primos es:", promedio/contador)
