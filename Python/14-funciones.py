def hola():
    print("hola mundo!")
    print("Ultimate Python")


hola()

#ARGUMENTOS Y PARAMETROS
print("\n --- ARGUMENTOS Y PARAMETROS --- ")
def hola2(nombre, apellido):
    print("hola mundo!".title())
    print(f"Bienvenido {nombre} {apellido}")


hola2("Rodrigo","Donoso")
hola2("Chanchito" ,"feliz")


#ARGUMENTOS OPCIONALES
print("\n --- ARGUMENTOS OPCIONALES --- ")
def hola3(nombre, apellido = "Feliz"): #PARAMETRO POR DEFECTO SI NO LE PASO UN ARGUMENTO
    print("hola mundo!".title())
    print(f"Bienvenido {nombre} {apellido}")


hola3("Chanchito" ,"Donoso")
hola3("Chanchito")

#ARGUMENTOS NOMBRADOS
print("\n --- ARGUMENTOS NOMBRADOS --- ")
def hola4(apellido, nombre):
    print("hola mundo!".title())
    print(f"Bienvenido {nombre} {apellido}")


hola4(apellido = "Donoso", nombre = "Chanchito")
hola4(apellido = "Donoso", nombre = "pERRIN")