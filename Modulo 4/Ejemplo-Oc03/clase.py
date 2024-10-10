class Vehiculo:
    # marca ="Nissan"
    # color= "azul"
    # tipo = "auto"
    cantidad_de_ruedas = 4
    posicion = 0

    def __init__(self, marca, color, tipo):
        self.marca = marca
        self.color = color
        self.tipo = tipo

    def avanzar(self, metros): 
        self.posicion += metros
        

    def retroceder():
        pass

    def virar():
        pass

auto1=Vehiculo("Nissan","azul","auto")
print(auto1.cantidad_de_ruedas)
print(auto1.marca)

print("Posicion inicial: ", auto1.posicion)

auto1.avanzar(15)
print("Posicion intermedia: ", auto1.posicion)

auto1.posicion += 5
print("Posicion final: ", auto1.posicion)