#Diccionario, es una colección de pares clave-valor

punto = {"x": 25, "y": 50}

print(punto) #imprime todo el diccionario
print(punto["x"]) #imprime el valor de la clave x
print(punto["y"]) #imprime el valor de la clave y

punto["z"] = 45 #agrega una clave-z con valor 45
print(punto)

if "j" in punto:
    print("Existe la clave j")
else:
    print("No existe la clave j")

print(punto.get("x")) #imprime el valor de la clave x
print(punto.get("j",97)) #imprime el valor de la clave j

print(punto)

del punto["x"] #elimina la clave-x
print(punto)

del (punto["y"]) #elimina la clave-y
print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for clave, valor in punto.items():
    print(clave, valor)

usuarios =[
    {"id": 1, "nombre": "Wolfgang"},
    {"id": 2, "nombre": "Melvin"},
    {"id": 3, "nombre": "Chanchito feliz"},
    {"id": 4, "nombre": "Chanchito triste"},
]

for usuario in usuarios: #imprime todos los usuarios
    print(usuario["nombre"])
