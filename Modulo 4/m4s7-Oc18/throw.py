from exception_personalizada import EdadNoNegativa

edad = int(input("Ingresa tu edad:"))

try:
    if (edad < 0):
        raise EdadNoNegativa("Edad no puede ser negativa")
    else:
        print(f"Edad registrada { edad }")
except EdadNoNegativa as err:
    print(f"Error: {err}")

print("Fin del programa")