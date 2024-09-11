"""Sumar números pares e impares por separado
Escribe un programa que sume todos los números pares e impares del 1 al 50 por
separado y muestre ambos resultados"""

suma_par = 0
suma_impar = 0
for i in range(1,51):
    if i % 2 == 0:
        print(f"El número {i} es par")
        suma_par += i
    else:
        print(f"El número {i} es impar")
        suma_impar += i

print(f"La suma de los pares es: {suma_par}",sep="\n")
print(f"La suma de los impares es: {suma_impar}")