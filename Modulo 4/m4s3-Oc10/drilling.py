class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def movimiento(self):
        print(f"{self.nombre} está caminando")

class Ciclista(Persona):
    
    def movimiento(self,tipo_bicicleta=None):
        if tipo_bicicleta == None:
            super().movimiento()
        else:
            print(f"{self.nombre} está rodando en una bicicleta {tipo_bicicleta}")


class Maratonista(Persona):
    
    def movimiento(self,ritmo=None):
        if ritmo == None:
            super().movimiento()
        elif ritmo == "corriendo":
            print(f"{self.nombre} está {ritmo}")
        else:
            print(f"{self.nombre} trotando")

persona1 = Persona("Diego")
ciclista = Ciclista("Genesis")
maratonista = Maratonista("Rodrigo")


#persona1.movimiento()
ciclista.movimiento()
ciclista.movimiento("deportiva")

maratonista.movimiento()
maratonista.movimiento("corriendo")
maratonista.movimiento("cualquier otra cosa")

