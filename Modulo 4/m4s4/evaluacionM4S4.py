"""EJERCICIOS:
1. Defina una clase que contiene el objeto Persona con un solo atributo nombre. Luego, se
crean dos subclases: Maratonista y Ciclista, que pertenecen a la clase Persona.
2. Cada Clase contiene un método que se llama movimiento. Para el caso de la Persona, el
estado de movimiento es “caminando”, para el caso del Maratonista es “trotando”, y para
el caso del Ciclista es “rodando”.
3. Diseñe la clase en Python que refleje la herencia antes descrita."""


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def movimiento(self):
        print(f"{self.nombre} esta Caminando")


class Maratonista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def movimiento(self,ritmo=None):
        if ritmo == "None":
            super().movimiento()
        elif ritmo == "corriendo":
            print(f"{self.nombre} esta {ritmo}")
        else: 
            print("Trotando")


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def movimiento(self,tipo_bicicleta=None):
        if tipo_bicicleta == "None":
            super().movimiento()
        else:
            print(f"{self.nombre} esta Rodando en una bici {tipo_bicicleta}")

persona = Persona("Juan")
maratonista = Maratonista("Pedro")
ciclista = Ciclista("Maria")

persona.movimiento()
maratonista.movimiento()
ciclista.movimiento()