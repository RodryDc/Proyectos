#juego de adivinanza
import random
numero_secreto = random.randint(1, 10)
adivinado = False

while not adivinado:
    respuesta = int(input("Adivina un numero entre 1 y 10: "))
    if respuesta == numero_secreto:
        print("Felicidades, adivinaste el numero")
        adivinado = True
    elif respuesta < numero_secreto:
        print("Intenta de nuevo, el numero es mayor")    
    else:
        print("Intenta de nuevo, el numero es menor")