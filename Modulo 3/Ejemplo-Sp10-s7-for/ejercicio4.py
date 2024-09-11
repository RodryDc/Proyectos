"""Crear una lista de cuadrados
Dada la lista [1, 2, 3, 4, 5] , escribe un programa que cree una nueva lista donde
cada número sea el cuadrado del número original. Luego imprime la nueva lista."""

lista = [1,2,3,4,5]
nueva = []

for i in lista:
    cuadrado = i**2
    nueva.append(cuadrado)

print(f"La nueva lista es: {nueva} que es el cuadrado de la lista original")