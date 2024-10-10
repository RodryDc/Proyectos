#FILAS FIFO
from collections import deque

print("FILAS")
filas = deque([1,2])

filas.append(3)
filas.append(4)
filas.append(5)

print(filas)

filas.popleft()

print(filas)

if not filas:
    print("la lista esta vacia")

#PILAS LIFO
print("PILAS")
pilas = []

pilas.append(1)
pilas.append(2)
pilas.append(3)

print(pilas)

ultimoElemento = pilas.pop()

print(ultimoElemento)
print(pilas)
print(pilas[-1])

if not pilas:
    print("la pila esta vacia")

