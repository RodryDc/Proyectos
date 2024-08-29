#import matematicas.aritmetica as mate
from matematicas.aritmetica import sumar
import math

num1 =4
num2 =3

suma = sumar(num1,num2)

#resta = restar(num1,num2)

print(suma,sep="\n")

nombre ="carlos"

print("hola,", nombre)
print(f"hola, {nombre}") 

var_global = 10

def funcion():
    var_local = 20
    print(var_local)

funcion()


mi_lista = [1, "hola", 3.14]

print(mi_lista[1])


#Tuplas son inmutables, no pueden ser modificadas
mi_tupla = (1, "hola", 3.14)

print(mi_tupla[1])


#Diccionarios tiene metodos get(), keys(), values(), items(), update(), clear()
mi_diccionario = {
    "nombre": "Ana",
    "edad": 30
}

print(mi_diccionario["nombre"])

#set es inmutable y no permite duplicados
mi_set = {1, 2, 3, 1, 2, 3}

print(mi_set)

set_vacio = set()

print(set_vacio)

var1 = 35
var2= 200
var3 = 300

if var3<100:
    print("el numero es menor que 100")
elif var3>100 and var3 < 300:
    print("el numero es mayor que 100 y menor que 300")
else:
    print("el numero es mayor que 100")


mi_otra_lista =[]

for i in range(5):
    mi_otra_lista.append(i)

print(mi_otra_lista)

while len(mi_otra_lista) <10:
    mi_otra_lista.append("texto")

print(mi_otra_lista)