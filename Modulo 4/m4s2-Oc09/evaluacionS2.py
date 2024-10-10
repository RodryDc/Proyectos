"""EJERCICIO:
Implementar en Python la clase Persona, que tenga como atributos: nombre, apellidos, sexo, edad,
estatura y peso. Adicionalmente, se deben implementar los métodos get y set que modifiquen todos
los atributos antes mencionados de la clase persona, recordando que los métodos get son los
métodos que permiten acceder al estado del objeto persona, y los métodos set permiten modificar
el estado de dicho objeto.
Cree dos objetos de la instancia persona con los siguientes datos:
Persona_ 1: Pedro, Vivas, Masculino, 20 años, 1.78 mts, 68 Kg.
Persona_ 2: Juan, Camargo, Masculino. 18, 1.8 mts, 75 Kg.
Modifique en la Persona_1 su edad a 21 años, y a la Persona_2 el apellido a Santiago, y que se
muestre por pantalla las actualizaciones respectivas. """


class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def get(self):
        return self.apellidos

    def set(self, apellidos):
        self.apellidos = apellidos


persona1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)

persona1.edad = 21
persona2.apellidos = "Santiago"

print(persona1.edad)
print(persona2.apellidos)