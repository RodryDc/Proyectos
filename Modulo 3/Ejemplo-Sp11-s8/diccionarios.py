"""
Los diccionarios son colecciones desordenadas de pares clave-valor.
Cada elemento en el diccionario tiene una clave y un valor asociado
"""

#Sintaxis
mi_diccionario = {}
mi_diccionario2 = dict()

#Ejemplo
#nombre_diccionario = {clave:valor}
frutas = {"manzana": 100, "pera":150, "naranja":200}

#Acceder a elementos
print(frutas["naranja"]) #imprime 100

#Metodos
#get() busca un elemento dado su clave
print("\nGet")
print(frutas.get("naranja")) #imprime 100

#items() devuelve una lista de tuplas (clave, valor)
print("\nItems")
print(frutas.items()) #imprime una lista de tuplas (clave, valor)

lista = list(frutas.items())
print(lista[0])

#keys() devuelve una lista con las claves
print("\nKeys")
print(frutas.keys()) #imprime una lista con las claves

#values() devuelve una lista con los valores
print("\nValues")
print(frutas.values()) #imprime una lista con los valores

#update() agrega un elemento a un diccionario
print("\nUpdate")
frutas.update({"uva": 50, "mango": 300})
print(frutas)