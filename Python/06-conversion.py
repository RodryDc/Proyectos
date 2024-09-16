resultado = input("Ingresa tu edad: ") #devuelve una cadena

print("Tu edad es: ", type(resultado), resultado)

numero= int(resultado) #convierte a entero
str(22) #convierte a cadena
float("22.13") #convierte a flotante
bool("un string") #convierte a boolean, evalua en falso cuando el string es (0, "", None, False)

print("Tu edad es: ", numero + 2)

x = input("")

#int(x) transforma el valor en entero
#float(x) transforma el valor en flotante
#bool(x) evalua en falso cuando el string es (0, "", None, False)
#str(x) transforma el valor en string

print(bool("")) #devuelve False porque el string es (0, "", None, False)
print(bool("0")) #devuelve True porque el string que contiene el valor de 0
print(bool(None)) #devuelve False
print(bool(" ")) #devuelve True
print(bool(0)) #devuelve False 
print(bool(1)) #devuelve True porque es un entero