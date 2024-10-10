class Vehiculo:

    cantidad_de_ruedas = 4
    posicion = 0

    def __init__(self, marca, color, tipo):
        self.marca = marca
        self.color = color
        self.tipo = tipo

    def avanzar(self, metros):
        self.posicion = metros
        print("el vehículo avanzó")

    def retroceder(self):
        pass

    def virar(self):
        pass

auto1 = Vehiculo("Nissan","azul","auto")

auto2 = Vehiculo()

print(auto1.cantidad_de_ruedas)
print(auto1.marca)

print("Posición inicial")
print(auto1.posicion)

auto1.avanzar(15)

print("Posición final")
print(auto1.posicion)
