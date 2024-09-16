"""Crear una función con parámetros por defecto
Escribe una función llamada saludar() que reciba un parámetro nombre y devuelva un
saludo personalizado. Si no se proporciona ningún nombre, debe usar "invitado" como
valor por defecto.
Entrada:
saludar()
# "Hola, invitado!"
saludar("Ana")
# "Hola, Ana!"
Salida:
"Hola, invitado!"
"Hola, Ana!"""

def saludar(nombre="invitado"):
    return f"Hola, {nombre}!"

print(saludar())
print(saludar("Ana"))