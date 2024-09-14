"""Crear un perfil de usuario con `kwargs`**
Escribe una función llamada crear_perfil_usuario() que reciba una cantidad variable
de argumentos con nombre utilizando **kwargs . La función debe imprimir el perfil del
usuario.
Entrada:
crear_perfil_usuario(nombre="Juan", edad=30, ciudad="Madrid")
Salida:
Nombre: Juan
Edad: 30
Ciudad: Madrid"""

def crear_perfil_usuario(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

crear_perfil_usuario(nombre="Juan", edad=30, ciudad="Madrid")


# *args(1,2,3) -> (1,2,3)

# **kwargs(edad=30, ciudad="Madrid") -> {'edad': 30, 'ciudad': 'Madrid'}