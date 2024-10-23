"""Partiendo de la actividad realizada en el Rebound Exercises, construya una función que lea el
contenido del archivo informacion.dat.
Teniendo como salida lo siguiente:
$ python ejercicio.py
El archivo informacion.dat ya existe, ha sido creado previamente
Datos de información en la línea 1
Datos de información en la línea 2
Datos de información en la línea 3
Datos de información en la línea 4
Datos de información en la línea 5"""
import os

try:
    if os.path.exists("informacion.dat"):
        print(f"El archivo informacion.dat ya existe, ha sido creado previamente")    
        with open("informacion.dat","r") as file:
            for linea in file:
                print(linea)
except Exception as e:
    print(f"Ha ocurrido un error: {e}")