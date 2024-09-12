#Clase Personaje
class Personaje: 

#constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
#metodos
#metodo imprimir atributos
    def atributos(self):
        print(f"\nNombre: {self.nombre}\nFuerza: {self.fuerza}\nInteligencia: {self.inteligencia}\nDefensa: {self.defensa}\nVida: {self.vida}")
#metodo subir nivel
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
#metodo esta vivo (saber si esta vivo el personaje)
    def esta_vivo(self):
        if self.vida > 0:
            return True
        else:
            return False
#avisar si el personaje ha muerto
    def morir(self):
        self.vida = 0
        print(f"El personaje {self.nombre} ha muerto")
#metodo daño de un personaje
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(f"El personaje {self.nombre} ha hecho {daño} de daño a {enemigo.nombre}")
        if enemigo.esta_vivo() == True:
            print(f"El personaje {enemigo.nombre} tiene {enemigo.vida} de vida")
        else:
            enemigo.morir()

    def get_fuerza(self):
        return self.fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza > 0:
            self.fuerza = fuerza
        else:
            print("La fuerza no puede ser negativa")
"""
mi_personaje = Personaje("Saitama", 10, 1, 5, 100) #creamos mi personaje 
mi_enemigo =Personaje("Enemigo ", 8, 5, 3, 5) #creamos el enemigo
mi_personaje.atributos() #imprimimos los atributos del personaje
mi_enemigo.atributos() #imprimimos los atributos del enemigo
#print(f"EL daño que le hago a mi enemigo es: {(mi_personaje.daño(mi_enemigo))}") #imprimimos el daño de mi personaje con el enemigo
mi_personaje.atacar(mi_enemigo) #atacamos al enemigo
mi_enemigo.atributos() #imprimimos los atributos del enemigo
mi_personaje.subir_nivel(1,2,0) #subimos el nivel fuerza, inteligencia y defensa
mi_personaje.atributos() #imprimimos los atributos
"""
class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion= int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if (opcion == 1):
            self.espada = 8
        elif (opcion == 2):
            self.espada = 10
        else:
            print("Opcion no valida")

    def atributos(self):
        super().atributos()
        print(f"Espada: {self.espada}")

    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
"""
guts=Guerrero("Guts", 20, 10, 10, 100,5)
guts.atributos()
print(guts.espada)
"""

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print(f"Libro: {self.libro}")

    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
"""
goku = Personaje("Goku", 20, 15, 10, 100)
guts = Guerrero("Guts", 20, 15, 10, 100, 5)
vanessa = Mago("Vanessa", 20, 15, 10, 100, 5)
print("antes del ataque")
goku.atributos()
guts.atributos()
vanessa.atributos()
goku.atacar(guts)
guts.atacar(vanessa)
vanessa.atacar(goku)
print("-------------------")
print("despues del ataque")
goku.atributos()
guts.atributos()
vanessa.atributos()
"""
#personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_1 = Personaje("Guts", 20, 10, 4, 100)
personaje_2= Mago("Vanessa", 5, 15, 4, 100, 3)

def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"Turno {turno}")
        print(f">>> Accion de {jugador_1.nombre} :", sep="")        
        jugador_1.atacar(jugador_2)
        print(f">>> Accion de {jugador_2.nombre} :", sep="")
        jugador_2.atacar(jugador_1)
        turno += 1

    if jugador_1.esta_vivo():
        print(f"{jugador_1.nombre} ha ganado")
    elif jugador_2.esta_vivo():
        print(f"{jugador_2.nombre} ha ganado")
    else:
        print("Empate")

combate(personaje_1, personaje_2)
"""
#POLIMORFISMO
class Cafe:
    def que_soy(self):
        print("Soy un cafe")

class Te:
    def que_soy(self):
        print("Soy un te")

def definicion_bebida(bebida):
    bebida.que_soy()

definicion_bebida(Cafe())
definicion_bebida(Te())
"""