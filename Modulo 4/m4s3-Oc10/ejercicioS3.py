"""EJERCICIO:
Realice un diagrama de clases que simule a una persona y a un estudiante. La persona contiene las
siguientes características: número de identificación, el nombre, el apellido. Mientras que el
estudiante contiene el número de identificación, el nombre, el apellido, código del alumno y matrícula.
Ambos poseen un método para obtener los datos. """


class Persona:
    def __init__(self, identificacion, nombre, apellido):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido

    def obtener_identificacion(self):
        return self.identificacion

    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido
    

class Estudiante(Persona):
    def __init__(self, identificacion, nombre, apellido, codigo, matricula):
        super().__init__(identificacion, nombre, apellido)
        self.codigo = codigo
        self.matricula = matricula

    def obtener_codigo(self):
        return self.codigo

    def obtener_matricula(self):
        return self.matricula
    
