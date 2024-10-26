#Parte 3
"""En esta tercera parte el cliente quiere que se guarden los datos en un archivo con el nombre de
vehiculos.csv, es decir, un archivo separado por comas.
Para esto se debe tener en cuenta el siguiente ejemplo de guía con relación a la manipulación de
objetos en los archivos csv:
1 from Vehiculo import Automovil
2 import csv
3
4 def guardar(nombre_archivo, Automovil):
5
archivo = open(nombre_archivo, "w")
6
datos = [(Automovil.__class__, Automovil.__dict__)]
7
archivo_csv = csv.writer(archivo)
8
archivo_csv.writerows(datos)
9
archivo.close()
10
11 def recuperar(nombre_archivo):
12
vehiculos = []
13
archivo = open(nombre_archivo, "r")
14
archivo_csv = csv.reader(archivo)
15
for vehiculo in archivo_csv:
16
vehiculos.append(vehiculo)
17
archivo.close()
18
return vehiculos
19
20 automovil = Automovil("Ford", "Fiesta", "4", "180", "500")
21
22 guardar("ejemplo.csv", automovil)
23
24 automoviles = recuperar("ejemplo.csv")
25
26 for automovil in automoviles:
27
print(automovil)
Salida del ejemplo:
$ python ejemplo_csv.py
["<class 'Vehiculo.Automovil'>", "{'marca': 'Ford', 'modelo':
'Fiesta', 'nro_ruedas': '4', 'velocidad': '180', 'cilindrada':
'500'}"]
Actividades en este parte 3:
●
Crear el método que permita guardar cada uno de los objetos previamente creados en el
archivo vehiculos.csv, el nombre del método es: guardar_datos_csv(self)
Tome como referencia los siguientes objetos:
1 particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
2 carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
3 bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
4 motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble
5 Viga", 21)
•
En el archivo vehiculos.cvs se guardan de la siguiente manera:
1 <class 'Vehiculo.Particular'>,"{'marca': 'Ford', 'modelo':
2 'Fiesta', 'nro_ruedas': '4', 'velocidad': '180', 'cilindraje':
3 '500', 'nro_puestos': '5'}"
4 <class 'Vehiculo.Carga'>,"{'marca': 'Daft Trucks', 'modelo': 'G
5 38', 'nro_ruedas': '10', 'velocidad': '120', 'cilindraje': '1000',
6 'carga': '20000'}"
7 <class 'Vehiculo.Bicicleta'>,"{'marca': 'Shimano', 'modelo': 'MT
8 Ranger', 'nro_ruedas': 2, 'tipo': 'Carrera'}"
9 <class 'Vehiculo.Motocicleta'>,"{'marca': 'BMW', 'modelo': 'F800s',
10 'nro_ruedas': 2, 'tipo': 'Deportiva', 'motor': '2T', 'cuadro':
11 'Doble Viga', 'nro
La estructura para guardar son la clase, y luego los atributos del objeto de la clase.
●
Cree un método que lea del archivo vehiculos.csv con el nombre leer_datos_csv(self) y
que imprima por pantalla o terminal lo siguiente según la clasificación del vehículo:
$ python main.py
Lista de Vehiculos Particular
{'marca': 'Ford', 'modelo': 'Fiesta', 'nro_ruedas': '4', 'velocidad':
'180', 'cilindrada': '500', 'nro_puestos': '5'}
Lista de Vehiculos Carga
{'marca': 'Daft Trucks', 'modelo': 'G 38', 'nro_ruedas': '10',
'velocidad': '120', 'cilindrada': '1000', 'carga': '20000'}
Lista de Vehiculos Bicicleta
{'marca': 'Shimano', 'modelo': 'MT Ranger', 'nro_ruedas': 2, 'tipo':
'Carrera'}
Lista de Vehiculos Motocicleta
{'marca': 'BMW', 'modelo': 'F800s', 'nro_ruedas': 2, 'tipo':
'Deportiva', 'motor': '2T', 'cuadro': 'Doble Viga', 'nro_radios': 21}
●
En los métodos creados utilice el manejo de excepciones en caso de errores en el
archivo."""

from Vehiculo import Automovil
import csv

def guardar(nombre_archivo, Automovil):
    archivo = open(nombre_archivo, "w")
    datos = [(Automovil.__class__, Automovil.__dict__)]
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerows(datos)
    archivo.close()

def recuperar(nombre_archivo):
    vehiculos = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    for vehiculo in archivo_csv:
        vehiculos.append(vehiculo)
    archivo.close()
    return vehiculos

automovil = Automovil("Ford", "Fiesta", "4", "180", "500")
guardar("ejemplo.csv", automovil)
automoviles = recuperar("ejemplo.csv")

for automovil in automoviles:
    print(automovil)