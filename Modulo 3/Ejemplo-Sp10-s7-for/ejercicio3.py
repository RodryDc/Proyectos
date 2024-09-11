"""Ejercicio 3: Contar vocales en una cadena
Escribe un programa que pida al usuario que ingrese una frase, y luego cuente cuántas
vocales (a, e, i, o, u) tiene la frase"""

frase = input("Ingresa una frase: ").lower()
vocales = 0

for letra in frase:
    if letra in "aeiou":
        vocales += 1    

print(f"La frase tiene {vocales} vocales")
