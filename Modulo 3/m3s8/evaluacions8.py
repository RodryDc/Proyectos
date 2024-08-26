(""")Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
[[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
• Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
• Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
• Finalmente, imprimiremos en pantalla el diccionario resultante.
Ejemplo de impresión en pantalla:
A:[1, 2, 3](""")


listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

for lista in listas:
    if lista[0] == 0:
        continue
    for i in range(len(lista)):
        if lista[i] == 0:
            break
    else:
        print(lista)

diccionario = {"A": listas[0], "B": listas[1], "C": listas[2], "D": listas[3]}

print("\nDiccionario:")
print(diccionario)

