# class A:
#     def imprimir(self):
#         print("Imprimiendo A")


# class B(A):
#     def imprimir(self):
#         print("Imprimiendo B")
#         super().imprimir() #Llamamos al metodo de la clase padre

# class C(B):
#     def imprimir(self):
#         print("Imprimiendo C")
#         super().imprimir()


# Obj = B()
# Obj2 = A()
# Obj3 = C()

# Obj3.imprimir()


# class A:
#     def imprimir(self):
#         print("Imprimiendo A")

#     def foo(self):
#         print("Metodo de clase A")
# class B(A):
#     def __init__(self,b):
#         self.b = b
#     def imprimir(self):
#         super().imprimir() #Llamamos al metodo de la clase padre
#         print("Imprimiendo B")
       

# class C(B):
#     def __init__(self,b,c):
#         super().__init__(b)
#         self.c = c
    
#     def imprimir(self):
#         super().imprimir()
#         print("Imprimiendo C")
        
#     def foo(self):
#         print("Metodo de clase C")

# class A:
#     def imprimir(self):
#         print("Imprimiendo A")

#     def foo(self):
#         print("Metodo de clase A")
# class B():
#     def __init__(self,b):
#         self.b = b
#     def imprimir(self):
#         #super().imprimir() #Llamamos al metodo de la clase padre
#         print("Imprimiendo B")
       

# class C(A,B):
#     def __init__(self,b,c):
#         super().__init__(b)
#         self.c = c
    
#     def imprimir(self):
#         super().imprimir()
#         print("Imprimiendo C")
        
    

class A:
    def imprimir(self):
        print("Imprimiendo A")

    def foo(self):
        print("Metodo de clase A")
class B(A):
    def __init__(self,b):
        self.b = b
    def imprimir(self):
        super().imprimir() #Llamamos al metodo de la clase padre
        print("Imprimiendo B")
       

class C(A):
    def __init__(self,c):
        self.c = c
    
    def imprimir(self):
        super().imprimir()
        print("Imprimiendo C")
        
class D(B,C):

    def imprimir(self):
        super().imprimir()
        print("Imprimiendo D")




Obj = B("b")
Obj2 = A()
Obj3 = C("c")
Obj4 = D("b")

print(D.__mro__)#Muestra el orden de los metodos
Obj4.imprimir()
# Obj3.imprimir()
# Obj.imprimir()
# Obj3.foo()

print(C.__bases__)