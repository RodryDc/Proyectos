class Vehiculo:
    def __init__(self, marca,modelo,color,peso,puestos):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.peso = peso
        self.puestos = puestos
    
    def arrancar(self):
        print("El vehiculo arrancó.")
    
    def frenar(self):
        print("El vehiculo frenó")

    def girar(self):
        print("El vehiculo giró")
    
    def acelerar(self):
        print("El vehiculo aceleró")
    
    def estacionar(self):
        print("El vehiculo estacionó")

class Carro(Vehiculo):

    def __init__(self,marca,modelo,color,peso,puestos,velocidad,cilindrada):
        super().__init__(marca,modelo,color,peso,puestos)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def arrancar(self):
        print(f"El carro arrancó ")

    def arrancar(self,forma):
        print(f"el carro arrancó con {forma}")

def arrancar_vehiculo(vehiculos):
    for vehiculo in vehiculos:
        vehiculo.arrancar()


carro = Carro("nissan","versa","rojo",2,5,250,2)
vehiculo = Vehiculo("nissan","versa","rojo",2,5)

print(carro.modelo)
#carro.arrancar()

#print(isinstance(vehiculo,Carro))

arrancar_vehiculo([carro,vehiculo])

carro.arrancar()