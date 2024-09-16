"""Reemplazar palabras en una cadena
Escribe una función llamada reemplazar_palabra() que reciba una cadena de texto, una
palabra objetivo y una palabra de reemplazo. La función debe devolver una nueva cadena
donde todas las ocurrencias de la palabra objetivo sean reemplazadas por la palabra de
reemplazo.
Entrada:
reemplazar_palabra("El perro corre rápido", "perro", "gato")
Salida:
"El gato corre rápido"""

def reemplazar_palabra(cadena, palabra_objetivo, palabra_reemplazo):
    return cadena.replace(palabra_objetivo, palabra_reemplazo)

print(reemplazar_palabra("El perro corre rápido", "perro", "gato"))