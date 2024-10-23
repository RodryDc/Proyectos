"""Diseñe un programa en Python que cree un archivo si no se encuentra; en caso de existir el
archivo, debe reflejar un mensaje que especifica que ya se encuentra el archivo previamente
creado.
El archivo por crear debe llamarse informacion.dat. el cual contiene lo siguiente:
Datos de información en la línea 1
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5"""

import os

if os.path.exists("informacion.dat"):
    print("El archivo ya existe")
else:
    with open("informacion.dat","w") as file:
        file.write("Dato de informacion en linea 1\n")
        file.write("Dato de informacion en linea 2\n")
        file.write("Dato de informacion en linea 3\n")
        file.write("Dato de informacion en linea 4\n")
        file.write("Dato de informacion en linea 5\n")