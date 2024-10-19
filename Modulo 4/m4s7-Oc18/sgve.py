"""ABPro: Sistema de Gestión de Vehículos para un Estacionamiento
Contexto:
Un estacionamiento está buscando una manera de automatizar la gestión de los vehículos
que ingresan, asegurando un control adecuado del tipo de vehículo, el tiempo de
permanencia y los pagos correspondientes. El sistema debe poder registrar diferentes
tipos de vehículos, calcular las tarifas y generar un resumen para el cliente.
Tu equipo ha sido asignado para desarrollar la estructura básica de este sistema, que
permita gestionar vehículos y calcular tarifas en función del tipo de vehículo y del
tiempo que permanecen en el estacionamiento.
Objetivo del Proyecto
El objetivo es implementar un sistema de gestión de vehículos que utilice herencia
simple y múltiple, excepciones personalizadas, y aplique conceptos avanzados como el
uso del decorador @dataclass , métodos dunder, y manejo de excepciones con try-
except . El sistema debe permitir registrar diferentes tipos de vehículos, calcular
tarifas según el tiempo de permanencia y generar un recibo para el cliente.
Requisitos del Sistema
1. Registrar vehículos: El sistema debe permitir registrar vehículos de diferentes
tipos, como automóviles y motocicletas.
2. Calcular tarifas: Las tarifas deben variar según el tipo de vehículo y el
tiempo de permanencia.
3. Generar recibo: El sistema debe generar un recibo que incluya el tipo de
vehículo, el tiempo de permanencia, y el total a pagar.
4. Manejo de errores: Implementar excepciones personalizadas y capturar errores
con try-except para manejar situaciones como "vehículo no encontrado" o
"tiempo de permanencia inválido".
Clases a Implementar
1. Clase Vehiculo
Esta clase será la base para todos los vehículos en el sistema. Utiliza el decorador
@dataclass .
Atributos:
placa : Placa del vehículo.
marca : Marca del vehículo.
Métodos dunder aplicables:
__str__ : Retorna la placa y la marca del vehículo.
2. Clase Automovil (herencia de Vehiculo )
Hereda de Vehiculo y representa un automóvil.
Atributos adicionales:
tarifa_por_hora : Tarifa por hora (por defecto, $2).
Métodos:
calcular_tarifa : Calcula la tarifa en función del tiempo de
permanencia.
3. Clase Motocicleta (herencia de Vehiculo )
Hereda de Vehiculo y representa una motocicleta.
Atributos adicionales:
tarifa_por_hora : Tarifa por hora (por defecto, $1).
Métodos:
calcular_tarifa : Calcula la tarifa en función del tiempo de
permanencia.
4. Clase Estacionamiento
Esta clase gestiona los vehículos que ingresan al estacionamiento.
Atributos:
vehiculos : Lista de vehículos registrados.
Métodos:
registrar_vehiculo : Agrega un vehículo a la lista de vehículos.
calcular_tarifa : Calcula la tarifa total para un vehículo dado su
tiempo de permanencia. Incluye manejo de excepciones para verificar que
el vehículo esté registrado y que el tiempo sea válido.
5. Clase Recibo
Genera un recibo para el cliente después de calcular la tarifa.
Atributos:
vehiculo : Vehículo que utilizó el estacionamiento.
tiempo : Tiempo de permanencia en horas.
total : Total a pagar.
Métodos:
__str__ : Genera un recibo con el tipo de vehículo, tiempo de
permanencia y el total a pagar.
6. Clase ControlDeTiempo (herencia múltiple de Automovil y Motocicleta )
Esta clase se encarga de verificar y calcular el tiempo de permanencia de cualquier
tipo de vehículo.
Métodos:
validar_tiempo : Verifica que el tiempo ingresado sea positivo. Si el
tiempo no es válido, lanza una excepción personalizada.
Excepciones Personalizadas
Debes crear las siguientes excepciones personalizadas para manejar errores en el
sistema:
TiempoInvalidoError: Se lanza cuando el tiempo de permanencia es negativo o no
válido.
VehiculoNoEncontradoError: Se lanza cuando se intenta calcular la tarifa de un
vehículo que no está registrado.
Pautas para el Desarrollo del Proyecto
1. Distribución de Tareas: Los estudiantes deben dividirse el trabajo de forma
equitativa. Un miembro puede encargarse de implementar la clase Vehiculo y las
clases derivadas, otro de Estacionamiento , y así sucesivamente.
2. Desarrollo y Pruebas: Desarrollen el sistema por partes y prueben cada una
antes de integrarla. Asegúrense de que las excepciones personalizadas se lancen
y manejen correctamente mediante bloques try-except .
Ejemplo de Funcionamiento Esperado
try:
# Crear instancia de Automóvil
auto = Automovil(placa="ABC123", marca="Toyota", tarifa_por_hora=2)
# Registrar automóvil en el estacionamiento
estacionamiento = Estacionamiento()
estacionamiento.registrar_vehiculo(auto)
# Calcular tarifa para un tiempo válido
tiempo = 3
# Horas
tarifa = estacionamiento.calcular_tarifa(auto, tiempo)
print(f"Tarifa calculada: {tarifa}")
# Generar recibo
recibo = Recibo(vehiculo=auto, tiempo=tiempo, total=tarifa)
print(recibo)
except TiempoInvalidoError as e:
print(f"Error: {e}")
except VehiculoNoEncontradoError as e:
print(f"Error: {e}")
Salida esperada:
Tarifa calculada: 6
Recibo:
Vehículo: Toyota, Placa: ABC123
Tiempo: 3 horas
Total a pagar: $6"""


from dataclasses import dataclass
from exception_personalizada import VehiculoNoEncontradoError, TiempoInvalidoError

@dataclass
class Vehiculo:
    placa : str
    marca : str

    def __str__(self):
        return f"La placa del vehiculo es {self.placa} y su marca {self.marca}"

@dataclass    
class Automovil(Vehiculo):
    tarifa_por_hora : int 

    def calcular_tarifa(self,tarifa_por_hora, tiempo):        
        return tarifa_por_hora * tiempo 

@dataclass   
class Motocicleta(Vehiculo):
    tarifa_por_hora : int 

    def calcular_tarifa(self,tarifa_por_hora, tiempo):        
        return tarifa_por_hora * tiempo 

class Estacionamiento:
    Vehiculos = []

    def registrar_vehiculo(self,vehiculo):
        self.Vehiculos.append(vehiculo)
        

    def calcular_tarifa(self,vehiculo,tiempo):
        try:
            return vehiculo.calcular_tarifa(vehiculo.tarifa_por_hora,tiempo)
        except Exception as e:
            raise e
@dataclass
class Recibo:
    vehiculo : Vehiculo
    tiempo : int
    total : int

    def __str__(self):
        return f"El vehiculo {self.vehiculo} ha estado {self.tiempo} horas y su total a pagar es de {self.total}"     
@dataclass    
class ControlDeTiempo(Automovil,Motocicleta):
    def validar_tiempo(self):
        pass


try:
    # Crear instancia de Automóvil
    auto = Automovil(placa="ABC123", marca="Toyota", tarifa_por_hora=2)
    # Registrar automóvil en el estacionamiento
    estacionamiento = Estacionamiento()
    estacionamiento.registrar_vehiculo(auto)
    # Calcular tarifa para un tiempo válido
    tiempo = 3
    # Horas
    tarifa = estacionamiento.calcular_tarifa(auto, tiempo)
    print(f"Tarifa calculada: {tarifa}")
    # Generar recibo
    recibo = Recibo(vehiculo=auto, tiempo=tiempo, total=tarifa)
    print(recibo)
except TiempoInvalidoError as e:
    print(f"Error: {e}")
except VehiculoNoEncontradoError as e:
    print(f"Error: {e}")
