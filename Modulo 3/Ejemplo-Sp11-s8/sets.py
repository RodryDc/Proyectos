"""
Los sets son colecciones desordenadas de elementos unicos, es decir, no pueden contener elementos duplicados. son mutables, pero los elementos que contiene debe ser inmutables (no puedes incluir listas, tuplas, diccionarios, etc.).
"""

#Sintaxis
mi_set = set()
mi_set2 = {}

#Ejemplo
#nombre_set = {elemento}
set1 = {1, 2, 3, 4, 5,6}
set2 = {4,5,6,7,8}

#Acceder a elementos
print(set1) #imprime {1, 2, 3, 4, 5, 6}

#Metodos
#add() agrega un elemento
print("\nAdd")
set1.add(10)
print(set1)
set2.add(40)
print(set2)

#update() agrega mas de un elemento a un set
print("\nUpdate")
set1.update(set2)
print(set1)

#remove() elimina un elemento
print("\nRemove")
set1.remove(4)
print(set1)

#discard() elimina un elemento 
print("\nDiscard")
set1.discard(10)
print(set1)

#pop() elimina un elemento aleatorio
print("\nPop")
set1.pop()
print(set1)

print(set1 | set2) #union
print(set1 & set2) #interseccion
print(set1 - set2) #diferencia
print(set1 ^ set2) #diferencia simetrica