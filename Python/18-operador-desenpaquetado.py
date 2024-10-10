lista =[1,2,3,4] #LISTA
print(1,2,3,4) #imprime sin desenpaquetar
print(*lista) #desenpaquetamos

lista2 = [5,6]


combinada = [*lista, *lista2] #desenpaquetamos dos listas
print(combinada)

otra = ["jelou",*lista, *lista2, 7, 8, 9]
print(otra)
def n(n1, n2, n3, n4):
    print(n1, n2, n3, n4)

punto1 = {"x":19, "y":"Hola"}
punto2 = {"y":15}

nuevoPunto= {**punto1, "lala":"mundo", **punto2, "z":"mundo"} #desenpaquetamos dos diccionarios
print(nuevoPunto)