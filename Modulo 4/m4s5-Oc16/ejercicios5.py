"""EJERCICIOS:
Para llevar a cabo esta actividad, comenzaremos con la base del siguiente código en Python:
1 class A:
2
def __init__(self):
3
print("Pertenezco a la clase A")
4
def metodo_a(self):
5
print("Método heredado de A")
6
7 class B:
8
def __init__(self):
9
print("Clase B")
10
def metodo_b(self):
11
print("Método heredado de B")
1. Construya una nueva clase C que tenga herencia múltiple de B y A respectivamente, y
que contenga el metodo_c que imprima por pantalla “Método de clase C”.
2. Cree un nuevo objeto C, y al instanciarlo y acceder a cada método: metodo_a, metodo_b
y metodo_c tenga como resultado lo siguiente:
1 Clase B
2 Método heredado de A
3 Método heredado de B
4 Método es de C"""

class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    
    def metodo_a(self):
        print("Método heredado de A")
class B:
    def __init__(self):
        print("Clase B")

    def metodo_b(self):
        print("Método heredado de B")

class C(B,A):
    def metodo_c(self):
        print("Metodo de clase C")


Obj= C()

Obj.metodo_a()
Obj.metodo_b()
Obj.metodo_c()
