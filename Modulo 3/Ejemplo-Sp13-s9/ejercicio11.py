"""Ordenar una lista de palabras por longitud
Escribe una función llamada ordenar_por_longitud() que reciba una lista de palabras y
las ordene en orden ascendente según su longitud.
Entrada:
ordenar_por_longitud(["perro", "gato", "elefante", "ratón"])
Salida:
["gato", "perro", "ratón", "elefante"]"""

def ordenar_por_longitud(cosas):
    return sorted(cosas, key=len)

print(ordenar_por_longitud(["perro", "gato", "elefante", "ratón"]))

