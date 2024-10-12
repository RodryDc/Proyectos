class Circulo:

    __PI =3.14159    

    def __init__(self,color):
        self.color = color

    def get_color(self):
        print(self.color)

    @classmethod
    def calcularArea(cls,radio): #cls = clase
        return cls.__PI * (radio**2)

    def calcular_area_instancia(self,radio):
        return self.__PI * (radio**2)


print(Circulo.calcularArea(3))

c1 = Circulo("rojo")
c1.PI = 4

print(c1.PI)
print(c1.calcularArea(3))

# c1.mostrarRadio()

# c1.modificarRadio(3)

