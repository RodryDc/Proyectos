lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]

i=1
while i <= 5: 
    print(i) 
    i+=1

i=1
while i <= 5: 
    print(i * "el weta ") 
    i+=1

i=0
while i < len(lenguajes):
    print(lenguajes[i])
    i+=1

print("---")
numero = 1
while numero <= 100:
    print(numero)
    numero *= 2

comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print("Ejecutando: ", comando)

while True:
    comando = input("$ ")
    print("Ejecutando: ", comando)
    if comando.lower() == "salir":
        break