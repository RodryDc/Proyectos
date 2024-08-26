texto = "Hola Mundo"
print(texto.upper()) #convierte a mayusculas
print(texto.lower()) #convierte a minusculas
print(texto.find("Mundo")) #busca una palabra devuelve la posicion o indice
nuevoTexto = (texto.replace("Mun", "Chanchito feliz")) #reemplaza una palabra
print(texto, nuevoTexto)
print("Mundo" in texto) #busca una palabra devuelve true o false si la encuentra