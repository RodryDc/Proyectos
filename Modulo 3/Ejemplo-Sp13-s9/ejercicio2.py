"""Comprobar si un número es par o impar
Escribe una función llamada es_par() que reciba un número como parámetro y devuelva
True si es par y False si es impar.
Entrada:
es_par(4)
Salida:
True"""

def es_par(numero):
    return numero % 2 == 0

def es_numero_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(4))