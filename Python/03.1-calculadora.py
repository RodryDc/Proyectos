n1 = input("Ingresa el primer número: ")
n2 = input("Ingresa el segundo número: ")

n1 = int(n1) #convertimos a entero
n2 = int(n2) #convertimos a entero

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2
potencia = n1 ** n2
modulo = n1 % n2

mensaje =f"""
Para {n1} y {n2} el resultado es:
Suma: {suma}
Resta: {resta}
Multiplicacion: {multiplicacion}
Division: {division}
Potencia: {potencia}
Modulo: {modulo}
"""
print(mensaje)

print(mensaje.format(n1, n2, suma, resta, multiplicacion, division, potencia, modulo))

print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicacion: ", multiplicacion)
print("Division: ", division)
print("Potencia: ", potencia)
print("Modulo: ", modulo)