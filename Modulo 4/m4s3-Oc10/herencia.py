class Vehiculo:
    def __init__(self, marca, modelo, color, peso, puestos):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.peso = peso
        self.puestos = puestos

    def arrancar(self):
        print("El vehiculo Arranco")

    def frenar(self):
        print("El vehiculo Freno")

    def girar(self):
        print("El vehiculo Giro")

    def acelerar(self):
        print("El vehiculo Acelero")

    def estacionar(self):
        print("El vehiculo Estaciono")

class Carro(Vehiculo):
    def __init__(self, marca, modelo, color, peso, puestos, velocidad,cilindrada):
        super().__init__(marca, modelo, color, peso, puestos)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def arrancar(self):
        print("El carro Arranco")
        
carro=Carro("Toyota", "Yaris", "Rojo", 1000, 4, "Gasolina", 2.0)
vehiculo = Vehiculo("Toyota", "Yaris", "Rojo", 1000, 4)

print(carro.marca)
carro.arrancar()