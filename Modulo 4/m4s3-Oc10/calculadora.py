class Calculadora:
    tamano_pantalla = 3

    def __init__(self,color,marca,tipo):
        self.color = color
        self.marca = marca
        self.tipo = tipo
    
    @staticmethod
    def suma(num1, num2):
        return num1 + num2
    
    @staticmethod
    def resta(num1, num2):
        return num1 - num2
    

