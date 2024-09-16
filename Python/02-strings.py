texto = "Hola Mundo"
print(texto.upper()) #convierte a mayusculas
print(texto.lower()) #convierte a minusculas
print(texto.find("Mundo")) #busca una palabra devuelve la posicion o indice
nuevoTexto = (texto.replace("Mun", "Chanchito feliz")) #reemplaza una palabra
print(texto, nuevoTexto)
print("Mundo" in texto) #busca una palabra devuelve true o false si la encuentra

#METODOS

animal = "chanCHito feliz"
animal2= "   chanchito feliz   "

print("upper:", animal.upper()) #convierte a mayusculas
print("lower:", animal.lower()) #convierte a minusculas
print("capitalize:", animal.capitalize()) #convierte la primer letra en mayuscula
print("title:", animal.title()) #convierte la primer letra de cada palabra en mayuscula
print("strip:", animal2.strip()) #quita los espacios al inicio y final
print("lstrip:", animal2.lstrip()) #quita los espacios al inicio
print("rstrip:", animal2.rstrip()) #quita los espacios al final
print("find:", animal2.find("Chanchito")) #busca una palabra devuelve la posicion o indice
print("replace:", animal.replace("nCH", "g")) #reemplaza una palabra
print("in", "Chanchito feliz" in animal) #busca una palabra devuelve true o false si la encuentra
print("not in", "Chanchito feliz" not in animal) #busca una palabra devuelve true o false si la encuentra (inverso)
print("count:", animal2.count("Chanchito")) #devuelve el numero de veces que aparece una palabra
print("isnumeric:", animal2.isnumeric()) #devuelve true o false si es numerico
print("strip y capitalize:", animal2.strip().capitalize()) #quita los espacios al inicio y final y convierte la primer letra de cada palabra en mayuscula

#'' comilla simple
#"" comilla doble
#""" triple 
#\n salto de linea
#\\ barra invertida
#\$ signo de dolar
#\\t tabulador
#\"" comilla doble doble

print("\"hola mundo\"")
print("\"hola mundo\"".strip()) #quita los espacios al inicio y final
