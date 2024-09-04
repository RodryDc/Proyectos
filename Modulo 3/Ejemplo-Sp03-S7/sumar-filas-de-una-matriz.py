#sumar filas de una matriz

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#con for
for i in range(len(matriz)):
    suma = 0
    for j in range(len(matriz[i])):
        suma += matriz[i][j]
    print(f"Suma de la fila {i+1}: {suma}")

#con while
fila = 0
while fila < len(matriz):
    suma_fila = 0
    columna = 0
    while columna < len(matriz[fila]):
        suma_fila += matriz[fila][columna]
        columna += 1
    print(f"Suma de la fila {fila+1}: {suma_fila}")
    fila += 1