resultado = input("Ingresa tu edad: ") #devuelve una cadena

print("Tu edad es: ", type(resultado), resultado)

numero= int(resultado) #convierte a entero
str(22) #convierte a cadena
float("22.13") #convierte a flotante
bool("un string") #convierte a boolean, evalua en falso cuando el string es (0, "", None, False)

print("Tu edad es: ", numero + 2)