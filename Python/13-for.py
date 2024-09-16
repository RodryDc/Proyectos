lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]

for lenguaje in lenguajes: #para cada lenguaje
    print(lenguaje)

for numero in range(5):
    print(numero, numero * "Hola Mundo")

print ("---")
buscar = 8
for num in range(5):
    print(num)
    if num == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No encontrado")


print("\n --- ")

for char in "Hola Mundo": #para cada caracter 
    print(char)


#LOOP ANIDADO
print("\n --- ")
for j in range(3):
    for i in range(2):
        print(f"({i}, {j})")