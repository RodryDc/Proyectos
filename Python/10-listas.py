numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #NUMEROS
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"] #LETRAS
palabras = ["chanchito", "mundo", "feliz", "amigo"] #PALABRAS
booleans = [True, False, False, True] #BOOLEAN
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #MATRIZ
ceros =[0,1]*10 #CREA UNA LISTA CON 10 CEROS

print(ceros)

alfanumerico = numeros + letras #UNIR LISTAS
print(alfanumerico)

rango = list(range(0, 11)) #RANGO DE 0 A 10
print("rango", rango)

chars = list("hola mundo") #LISTA DE CARACTERES
print("chars",chars)

lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
print(lenguajes) #imprime toda la lista

print(lenguajes[1]) #Ruby

lenguajes[1]="Go" #reemplaza Ruby por Go
print(lenguajes)

print(lenguajes[-3]) #imprime el elemento de la posicion -3, -2, -1

print(lenguajes[1:3]) #imprime desde la posicion 1 hasta la 3

print(lenguajes[:3]) #imprime desde la posicion 0 hasta la 3

print(lenguajes[1:]) #imprime desde la posicion 1 hasta el final