"""
Se propone realizar el modelado de las clases que permita simular el comportamiento que
tendrían los diferentes integrantes de la selección de fútbol; tanto los Futbolistas y el cuerpo
técnico (Entrenadores, Masajistas). Para visualizar este comportamiento, se definirán tres clases
que van a representar a objetos: Futbolista, Entrenador y Masajista. Cada uno de ellos poseen
ciertos datos y características que reflejan en los atributos, y una serie de acciones que son sus
métodos. Estos atributos y métodos se pueden observar en la siguiente estructura de diagrama
de clases:
Diseñe de manera óptima la herencia que se puede observar en los diagramas anteriores,
teniendo en cuenta los atributos comunes y métodos que nos permitan representar a la selección
de fútbol. Puede hacer uso de la herramienta Umbrello para modelar."""

class IntegranteSeleccionFutbol:
    def __init__(self,id,nombre,apellidos,edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def concentrarse(self):
        print(f"{self.nombre} {self.apellidos} {self.edad} va a concentrarse")

    def viajar(self):
        print(f"{self.nombre} {self.apellidos} {self.edad} va a viajar")

class Futbolista(IntegranteSeleccionFutbol):
    def __init__(self,id,nombre,apellidos,edad,dorsal,demarcacion):
        super().__init__(id,nombre,apellidos,edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion

    def jugarPartido(self):
        print(f"El jugador {self.nombre} de {self.edad} usa el dorsal {self.dorsal} y juega de {self.demarcacion} ")
        
    def entrenar(self):
        print(f"{self.nombre} {self.apellidos} va a entrenar")

class Entrenador(IntegranteSeleccionFutbol):
    def __init__(self,id,nombre,apellidos,edad,idFederacion):
        super().__init__(id,nombre,apellidos,edad)
        self.idFederacion = idFederacion

    def dirigirPartido(self):
        print(f"El entrenador {self.nombre} va a dirigir un partido")

    def dirigirEntrenamiento(self):
        print(f"El entrenador {self.nombre} va a dirigir un entrenamiento")

class Masajista(IntegranteSeleccionFutbol):
    def __init__(self,id,nombre,apellidos,edad,titulacion, annosExperiencia):
        super().__init__(id,nombre,apellidos,edad)
        self.titulacion = titulacion
        self.annosExperiencia = annosExperiencia

    def darMasajes(self):
        print(f"El masajista {self.nombre} {self.apellidos} va a dar masaje")

#Ejemplo
jugador1 = Futbolista(1,"Cristiano","Ronaldo","39","7","Delantero")
print(f"\nDatos del futbolista: \nNombre: {jugador1.nombre} \nApellidos: {jugador1.apellidos} \nEdad: {jugador1.edad} \nDorsal: {jugador1.dorsal} \nDemarcacion: {jugador1.demarcacion}")
jugador1.jugarPartido()
jugador1.entrenar()

entrenador1 = Entrenador(1,"Carlo","Ancellotti","65","1")
print(f"\nDatos del entrenador: \nNombre: {entrenador1.nombre} \nApellidos: {entrenador1.apellidos} \nEdad: {entrenador1.edad} \nId federacion: {entrenador1.idFederacion}")
entrenador1.dirigirPartido()
entrenador1.dirigirEntrenamiento()

masajista1 = Masajista(1,"Manuel","Pintus","48","Masajista","4")
print(f"\nDatos del masajista: \nNombre: {masajista1.nombre} \nApellidos: {masajista1.apellidos} \nEdad: {masajista1.edad} \nTitulacion: {masajista1.titulacion} \nAños de experiencia: {masajista1.annosExperiencia}")
masajista1.darMasajes()





