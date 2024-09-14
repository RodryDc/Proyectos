"""Contar vocales en una cadena
Escribe una función llamada contar_vocales() que reciba una cadena de texto y cuente
cuántas vocales (a, e, i, o, u) tiene.
Entrada:
contar_vocales("hola mundo")
Salida:
4"""

def contar_vocales(palabra):
    vocales = 0
    for letra in palabra:
        if letra.lower() in "aeiou":
            vocales += 1
    return vocales    
    
print(contar_vocales("hola mundo"))