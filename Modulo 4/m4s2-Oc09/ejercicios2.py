"""EJERCICIO:
Codifique en Python una clase que represente a un animal. Un animal tiene las siguientes
características comunes:
• Nombre.
• Raza.
• Edad.
• Peso.
Debe crear dos instancias u objetos de la clase Animal, cuyos objetos son un caballo y un león, con
las siguientes características particulares:
Caballo 
Nombre Zeus 
Edad 5 años 
Raza Pura sangre 
Peso 450 kg 

León
Nombre Boulder
Edad 10 años
Raza Atlas
Peso 130 kg"""

class Animal:
    def __init__(self,nombre,edad,raza,peso):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
    
    def mostrarAnimal(self):
        print(f"Nombre: {self.nombre}, edad: {self.edad} años, raza : {self.raza}, peso: {self.peso} kg")   

Caballo = Animal("Zeus",5,"Pura Sangre",450)
Leon = Animal("Boulder",10,"Atlas",130)

Caballo.mostrarAnimal()
Leon.mostrarAnimal()


