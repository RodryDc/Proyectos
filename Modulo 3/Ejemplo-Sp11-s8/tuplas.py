"""
Las tuplas son colecciones ordenadas pero inmutables, lo que significa que una vez creadas, no se pueden modificar (ni añadir,elminar o reemplazar elementos)."""

#Sintaxis
mi_tupla = ()
mi_tupla2 = tuple()

#Ejemplo
#nombre_tupla = (indice.elemento)
vocales = ("a","e","i","o","u")

mi_tupla = (1, 2, 3, ['rojo', 'verde'])

#Acceder a elementos
print(mi_tupla[3].append("azul")) #imprime ['rojo', 'verde'] + 'azul' porque append es un metodo para la lista
print(mi_tupla)
print(vocales[3]) #imprime o

#Metodos
#count() cuenta la cantidad de elementos que se repite
print("\nCount")
print(vocales.count("a")) #imprime la cantidad de elementos que se repite

#index() busca la posicion de un elemento dado
print("\nIndex")
print(vocales.index("e")) #imprime la posicion del elemento e 

#len() es una funcion que nos dice la cantidad de elementos
print("\nLen")
print(len(mi_tupla))

