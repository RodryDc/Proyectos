# 1.- Eliminar los espacios en blanco de un string y devolver una lista con los caracteres restante 
# 2.- Contar con un diccionario cuando se repiten los caracteres de un string
# 3.- Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene las tuplas [("a", 3), ("b",2), ("c", 4), ("d", 4)]
# 4.- En un listado de tuplas devolver las que tengan el mayor valor. [("a", 3), ("b", 2), ("c", 4)] -> [("c", 4), ("d", 4)]
# 5.- Crear un mensaje que diga: Los caracteres que mas se repiten con 4 repeticiones son :
# - C
# - D
# 6.- Juntar la solucion de los ejercicios anteriores para encontrar los caracteres que mas se repiten de un string

from pprint import pprint #Para imprimir listas

#texto = input("Ingresa un texto: ")
texto = "Hola Mundo este es mi string"

def quitar_espacios(texto):
    texto = texto.replace(" ", "")
    return list(texto)

def cuenta_caracteres(lista):
    diccionario = {}
    for char in lista:
        if char in diccionario:
            diccionario[char] += 1
        else:
            diccionario[char] = 1
    return diccionario

def ordena(elemento):
    return sorted(elemento.items(), key=lambda key: key[1], reverse=True)

def mayor_valor(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

def crea_mensaje(respuesta):
    mensaje ="Los caracteres que mas se repiten :\n"
    for key, valor in respuesta.items():
        mensaje += f"- {key} con {valor} repeticiones\n"
    return mensaje


print("\n Quitar espacios: ")
sin_espacios = quitar_espacios(texto)
print(sin_espacios)

print("\n Cuenta caracteres: ")
contados = cuenta_caracteres(sin_espacios)
pprint(contados,width=1)

print("\n Ordena caracteres: ")
ordenados = ordena(contados)
print(ordenados)

print("\n Mayor valor: ")
mayor = mayor_valor(ordenados)
print(mayor)

print("\n Crea mensaje: ")
mensaje = crea_mensaje(mayor)
print(mensaje)