(""")Requerimos crear una variable con el número 8, una con el número 10.5, y una con la palabra
“ejercicio”. Luego, crear un set que contendrá cada una de las variables que creamos, y será
asignado a una variable.
A continuación, crearemos una lista que contendrá el set creado anteriormente, y una variable con
el valor lógico False. Esta lista la asignaremos a una variable que luego imprimiremos en pantalla.(""")

a = 8 #Asignamos el valor 8 a la variable a
b = 10.5 #Asignamos el valor 10.5 a la variable b
c = "ejercicio" #Asignamos el valor "ejercicio" a la variable c
d = {a, b, c} #Asignamos el set d a la variable d
print(d) #Imprimimos el set d
e = [d, False] #Asignamos la lista e a la variable e
print(e) #Imprimimos la lista e