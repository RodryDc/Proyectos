"""
Las listas con colecciones ordenadas y mutables que permiten almacenar una secuencia de elementos. Los elementos pueden ser de cualquier tipo de datos, y las listas pueden contener otros objetos como listas anidadas, tuplas, diccionarios, etc.
"""
#Sintaxis
mi_lista = []
mi_lista2 = list()

#Ejemplo
#nombre_lista = [indice.elemento]
colores = ["azul","amarillo","rojo", "negro","azul", "rojo", "azul"]

#Acceder a elementos
print(colores[1]) #imprime amarillo

#Metodos
#count() cuenta la cantidad de elementos que se repite
print("\nCount")
print(colores.count("rojo")) #imprime la cantidad de elementos que se repite

#append() agrega un elemento al final de la lista
print("\nAppend")
colores.append("verde") #agrega al final
print(colores)

#remove() elimina primera coincidencia de un elemento dado el valor 
print("\nRemove")
colores.remove("rojo") #elimina un elemento
print(colores)

#insert() agrega un elemento en una posicion dada
print("\nInsert")
colores.insert(0,"naranja") #agrega un elemento en una posicion
print(colores)

#sort() ordena la lista de menor a mayor
print("\nSort")
colores.sort() #ordena la lista
print(colores)

#reverse() ordena la lista de mayor a menor
print("\nReverse")
colores.reverse() #invierte la lista
print(colores)
 
#extend() agrega una lista a la lista 
print("\nExtend")
otra_colores = ["rosado", "morado"] 
colores.extend(otra_colores) #agrega una lista
print(colores)

#index() busca la posicion de un elemento dado
print("\nIndex")
print(colores.index("azul"))

#copy()
print("\nCopy")
otra_colores = colores.copy() #copia la lista
print(otra_colores)

#len() es una funcion que nos dice la cantidad de elementos
print("\nLen")
print(len(colores)) #imprime la cantidad de elementos

#pop() elimina el ultimo elemento de una lista
print("\nPop")
colores.pop() #elimina el ultimo elemento
print(colores)

colores.pop(0) #elimina el primer elemento
print(colores)

#clear() elimina todos los elementos
print("\nClear")
colores.clear() #elimina todos los elementos
print(colores)