(""")Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for, e imprimir en
pantalla el valor de cada elemento indicando si es par, impar o cero.(""")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #Asignamos el valor a la variable numeros

for i in range(len(numeros)): #Recorremos la lista
    if (numeros[i] % 2 == 0): #Verificamos si el elemento es par
        print(numeros[i], "es par")
    elif (numeros[i] % 2 != 0): #Verificamos si el elemento es impar 
        print(numeros[i], "es impar")
    else: #Verificamos si el elemento es 0
        print(numeros[i], "es 0")

        