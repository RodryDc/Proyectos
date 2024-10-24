"""Diseñe un programa en Python que agregue el siguiente contenido al archivo: informacion.dat.
Hola Mundo
Este en una nueva línea en el archivo
agregando la segunda línea del archivo
finalizando la línea agregada
El nuevo archivo contiene la siguiente información:
Datos de información en la línea 1
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5
Este en una nueva línea en el archivo
agregando la segunda línea del archivo
finalizando la línea agregada"""

with open("informacion.dat", "a") as archivo:
    archivo.write("Hola Mundo\n")
    archivo.write("Este en una nueva línea en el archivo\n")
    archivo.write("agregando la segunda línea del archivo\n")
    archivo.write("finalizando la línea agregada\n")

    