class Clase: #Genero una plantilla para crear objetos
    atributo_clase = "valor por defecto"

    def __init__(self,parametro1,parametro2): #CONSTRUCTOR que recibe dos argumentos
        self.atributo_instancia = parametro1
        self.atributo_instancia2 = parametro2

    def metodo(self):
        print("Este es el metodo de la clase")

instancia = Clase("instancia1","instancia2")
print(instancia.atributo_clase)
instancia.atributo_clase = "nuevo valor"
print(instancia.atributo_clase)

print(Clase("valor_parametro1","valor_parametro2").atributo_clase) #OBJETO Clase

print(type(Clase("valor_parametro1","valor_parametro2")))

var = 3 #Objeto instanciado

3 #objeto suelto