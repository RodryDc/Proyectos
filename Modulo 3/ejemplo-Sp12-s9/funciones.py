def funcion():
    #codigo
    return "Hola Mundo"

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def saludo(nombre):
    print(f"Buenas tardes, {nombre}")

saludo("Carlos")

def multiplicar(num1, num2):
    num += 1
    return num1 * num2

num1= 5
num2 = 3

def desplegar_args(*args): #args = argumentos como listas
    for elemento in args:
        print(elemento)

def desplegar_lista(*lista):
    for elemento in lista:
        print(elemento)

# desplegar_lista(1,3,45,5,"Hola","mundo")

# print(num2,"hola",num1, "mundo",sep=" - ", end="Cadena final",)

def desplegar_diccionario(**kwargs): #kwargs = argumentos como diccionarios
    print(kwargs)

def mostrar_promedios(**kwargs):
    for nombre, promedio in kwargs.items():
        print(f"El promedio de {nombre} es {promedio}")

estudiantes = {
    "Juan": 4.0,
    "Maria": 6.0,
    "Pedro": 5.5
}

mostrar_promedios(**estudiantes)

mostrar_promedios(diego=4.0, juan=5.0, pedro=6.0) #clave=valor kwargs
desplegar_args(2,"hola",3,True)

