(""")En esta actividad trabajaremos con listas. Tomando la lista que se entrega a continuación, se
solicita realizar las siguientes acciones en el orden indicado:
1. Eliminar los elementos duplicados.
2. Ordenar la lista resultante en orden ascendente.
La lista es:
mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15](""")


mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

print("\nLista sin elementos duplicados:") 
mi_lista = list(set(mi_lista)) #Eliminamos los elementos duplicados
print(mi_lista)

print("\nLista ordenada:")
mi_lista.sort() #Ordenamos la lista en orden ascendente
print(mi_lista)