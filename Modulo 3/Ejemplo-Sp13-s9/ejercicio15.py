"""Agregar y eliminar elementos de un diccionario
Escribe una función llamada modificar_diccionario() que reciba un diccionario, una
clave y un valor, y agregue la clave y el valor al diccionario. Si la clave ya existe,
elimina esa clave del diccionario.
Entrada:
modificar_diccionario({"a": 1, "b": 2}, "c", 3)
Salida:
{"a": 1, "b": 2, "c": 3}
Entrada:
modificar_diccionario({"a": 1, "b": 2, "c": 3}, "b", 2)
Salida:
{"a": 1, "c": 3}"""

def modificar_diccionario(diccionario, clave, valor):
    if clave in diccionario:
        del diccionario[clave]
    diccionario[clave] = valor
    return diccionario

print(modificar_diccionario({"a": 1, "b": 2}, "c", 3))
print(modificar_diccionario({"a": 1, "b": 2, "c": 3}, "b", 2))