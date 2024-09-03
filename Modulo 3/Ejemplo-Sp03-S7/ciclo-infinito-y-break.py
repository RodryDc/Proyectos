#Ciclo infonito y break

contador = 0

while True:
    print(f"Contador: {contador}")
    contador += 1
    if contador == 10:
        break

#salto de pares con continue
contador=0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(f"Numero impar: {contador}")