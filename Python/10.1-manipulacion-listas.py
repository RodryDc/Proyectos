mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"] #CREAR LISTA
print(mascotas[0]) #Wolfgang
mascotas[0] = "Bicho" #REEMPLAZAR ELEMENTO
print(mascotas)
print(mascotas[:3]) #Bicho, Pelusa, Pelusa
print(mascotas[2:]) #Pulga, Copito
print(mascotas[-1]) #Copito
print(mascotas[::2]) #Bicho Pulga
print(mascotas[1::2]) #Pelusa Copito

numeros = list(range(21))
print(numeros[1::2]) #muestra los elementos impares
print(numeros[::2]) #muestra los elementos pares

#DESEMPAQUETAR LISTAS
numeros=[1,2,3]

# #FEO !
# primero = numeros[0] #primero = 1
# segundo = numeros[1] #segundo = 2
# tercero = numeros[2] #tercero = 3

# print(primero, segundo, tercero)

primero, segundo, tercero = numeros #primero = 1, segundo = 2, tercero = 3
print(primero, segundo, tercero)

primero, *otros = numeros #*otros = [2,3]
print(primero, otros) #1

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primero, segundo, *otros, penu, ultimo = numeros
print(segundo, penu, ultimo) 

#ITERAR LISTAS
mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"] #CREAR LISTA

for indice, mascota in enumerate(mascotas): #mascota = (0, "Pelusa")
    print(indice,mascota)


#BUSCAR ELEMENTO
mascotas = ["Pelusa","Wolfgang","Pulga", "Felipe","Wolfgang", "Chanchito feliz"] #CREAR LISTA
print("Pelusa" in mascotas) #True
print("Chanchito" in mascotas) #False

print(mascotas.count("Wolfgang")) #1
if "Wolfang" in mascotas:
    print(mascotas.index("Wolfgang")) #0


#AGREGAR ELEMENTOS
mascotas = ["Wolfgang","Pelusa","Pulga", "Felipe","Pulga", "Chanchito feliz"] #CREAR LISTA
mascotas.append("Chanchito triste") #AGREGAR ELEMENTO AL FINAL
print(mascotas)

mascotas.insert(1, "Melvin") #AGREGAR ELEMENTO EN UNA POSICION ESPECIFICA
print(mascotas)

mascotas.remove("Pulga") #ELIMINAR ELEMENTO
print(mascotas)

mascotas.pop() #ELIMINAR ULTIMO ELEMENTO
print(mascotas)

mascotas.pop(1) #ELIMINAR ELEMENTO EN UNA POSICION ESPECIFICA
print(mascotas)

del mascotas[0] #ELIMINAR ELEMENTO EN UNA POSICION ESPECIFICA
print(mascotas)

mascotas.clear() #ELIMINAR TODOS LOS ELEMENTOS
print(mascotas)