"""Diseñar una clase que represente a un animal. Un animal tiene las siguientes características
comunes:
• Nombre.
• Raza.
• Edad.
• Peso.
Además, cada animal puede comer, caminar, dormir.
Adicionalmente, se debe representar a dos objetos que pertenecen a la clase animal, cuyos
objetos son un gato y un perro con las siguientes características particulares:
• Perro:
o Nombre: Brando.
o Edad: 3 años.
o Raza: San Bernardo.
o Peso: 30 kg.

• Gato:
o Nombre: Roll.
o Edad: 4 años.
o Raza: Persa.
o Peso: 3 kg."""

class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def comer(self):
        print(f"{self.nombre} come")

    def caminar(self):
        print(f"{self.nombre} camina")

    def dormir(self):
        print(f"{self.nombre} duerme")

perro = Animal("Brando","San Bernardo","3 años","30 kg")
gato = Animal("Roll","Persa","4 años","3 kg")

print("\nAnimales:")
print(f"\nPerro: \nNombre: {perro.nombre} \nRaza: {perro.raza} \nEdad: {perro.edad} \nPeso: {perro.peso}")
perro.comer() 
perro.caminar()
perro.dormir()
print(f"\nGato: \nNombre: {gato.nombre} \nRaza: {gato.raza} \nEdad: {gato.edad} \nPeso: {gato.peso}")
gato.comer()
gato.caminar()
gato.dormir()