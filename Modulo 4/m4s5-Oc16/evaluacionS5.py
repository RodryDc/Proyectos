"""EJERCICIOS:
Construya las siguientes clases, con los siguientes atributos:
● Persona
○ nombre
○ apellido
○ anno
● Departamento
○ nombre_dpto
○ nombre_corto_dpto
● Trabajador (Persona, Departamento)
○ nombre
○ apellido
○ anno
○ nombre_dpto
○ nombre_corto_dpto
○ salario
Construya el objeto trabajador con los siguientes datos:
○ nombre: Juan
○ apellido: Pérez
○ anno: 2005
○ nombre_dpto: Ingeniería de software
○ nombre_corto_dpto: IS
○ salario: 20000
Agregue el método __init__() a la clase Trabajador para establecer todos los atributos de las
clases Persona y Departamento. Por ejemplo:
1 print(trabajador.__dict__)
Y verificar la instancia del Trabajador con respecto a Persona, Departamento y Trabajador.
La salida final es:
1
2
3
4
5
6
7
$ python ejercicio.py
{'nombre': 'Juan', 'apellido': 'Pérez', 'anno': 2005, 'nombre_dpto':
'Ingenieria de Software', 'nombre_corto_dpto': 'IS', 'salario':
20000}
Es trabajador instancia de Persona: True
Es trabajador instancia de Departamento: True
Es trabajador instancia de Trabajador: True"""

class Persona:
    def __init__(self,nombre,apellido,anno):
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno

class Departamento:
    def __init__(self,nombre_dpto, nombre_corto_dpto):
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto

class Trabajador(Persona, Departamento):
    def __init__(self,nombre,apellido,anno,nombre_dpto,nombre_corto_dpto,salario):
        Persona.__init__(self,nombre,apellido,anno)
        Departamento.__init__(self,nombre_dpto, nombre_corto_dpto)
        self.salario = salario

trabajador= Trabajador("Juan","Pérez",2005,"Ingeniería de software","IS",20000)
print(trabajador.__dict__)
print(f"El trabajador es instancia de Persona: {isinstance(trabajador,Persona)}")
print(f"El trabajador es instancia de Departamento: {isinstance(trabajador,Departamento)}")
print(f"El trabajador es instancia de Trabajador: {isinstance(trabajador,Trabajador)}")