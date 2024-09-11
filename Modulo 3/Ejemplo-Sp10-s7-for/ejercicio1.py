"""Contar múltiplos de un número
Escribe un programa que cuente cuántos números entre 1 y 100 son múltiplos de 3. Luego
imprime el resultado."""

contador = 0
for i in range(1, 100):
    if i % 3 == 0:
        print(f"{i} es multiplo de 3")
        contador += 1
print(f"La cantidad de números es: {contador}")


