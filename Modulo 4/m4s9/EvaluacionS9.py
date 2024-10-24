"""Partiendo del ejercicio anterior (Rebound Exercises), construya una función que reemplace el
contenido de “Información” por “Procesamiento”, e imprima cuántos reemplazos realizó en el
archivo.
Teniendo como salida lo siguiente:
$ $ python ejercicio.py
Se realizaron: 5 remplazos
El contenido del archivo informacion.dat es:
Datos de Procesamiento en la línea 1
Datos de Procesamiento en la línea 2
Datos de Procesamiento en la línea 3
Datos de Procesamiento en la línea 4
Datos de Procesamiento en la línea 5
Este en una nueva línea en el archivo
agregando la segunda línea del archivo
finalizando la línea agregada"""


with open("informacion.dat", "r+") as archivo:
    contenido = archivo.read()
    contenido = contenido.replace("Información", "Procesamiento")
    archivo.seek(0)
    archivo.write(contenido)
    archivo.truncate()

    