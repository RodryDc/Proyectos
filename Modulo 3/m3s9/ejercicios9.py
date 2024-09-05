(""")Crear una función que acepte dos parámetros (base y altura) y calcule el área de un rectángulo.
Validar que ambos sean números positivos.(""")

def area_rectangulo(base, altura):
    if base > 0 and altura > 0:
        return base * altura
    else:
        return "Los datos no son correctos"

base = int(input("Ingresa la base: "))
altura = int(input("Ingresa la altura: "))

print("El área del rectángulo es: ", area_rectangulo(base, altura))
