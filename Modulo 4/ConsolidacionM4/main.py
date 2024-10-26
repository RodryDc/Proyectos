from Vehiculo import *

while True:
    print("\n--------------------------------------------")
    print("Bienvenido al sistema de control de vehiculos")
    print("Que parte desea probar?")
    print("1. Parte 1")
    print("2. Parte 2")
    print("3. Parte 3")
    print("4. Salir")   
    opcion = int(input("Ingrese la opcion deseada: "))
    

    match opcion:
        case 1:
            print("\nEjecutando Parte 1")
            #Ingreso de datos por teclado
            opcion = int(input("Cuantos Vehiculos desea insertar: "))
            automovil = []
            for i in range(opcion):
                print("\nDatos del automóvil", i+1)
                marca = input("Inserte la marca del automóvil: ")
                modelo = input("Inserte el modelo: ")
                num_ruedas = int(input("Inserte el número de ruedas:"))
                velocidad = int(input("Inserte la velocidad en km/h: "))
                cilindraje = int(input("Inserte el cilindraje en cc: "))
                automovil.append(Automovil(marca, modelo, num_ruedas, velocidad, cilindraje))

            #Impresión de datos
            print("\nImprimiendo por pantalla los Vehículos:\n")
            for i in range(len(automovil)):
                print(f"Datos del automóvil {i+1} : {automovil[i]}")
            
        case 2:
            print("\nEjecutando Parte 2")
            #Ingreso de datos
            particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
            carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
            bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
            motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

            #Impresión de datos
            print()
            print(particular)
            print(carga)
            print(bicicleta)
            print(motocicleta)

            #Impresión de instancias
            print()
            print("Motocicleta es instancia con relación a Vehículo: ", isinstance(motocicleta, Vehiculo))
            print("Motocicleta es instancia con relacion a Automovil: ", isinstance(motocicleta, Automovil))
            print("Motocicleta es instancia con relacion a Vehículo Particular: ", isinstance(motocicleta, Particular))
            print("Motocicleta es instancia con relacion a Vehículo de Carga: ", isinstance(motocicleta, Carga))
            print("Motocicleta es instancia con relacion a Bicicleta: ", isinstance(motocicleta, Bicicleta))
            print("Motocicleta es instancia con relacion a Motocicleta: ", isinstance(motocicleta, Motocicleta))
                        
        case 3:
            print("\nEjecutando Parte 3")
            particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
            carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
            bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
            motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
            guardar_datos_csv(particular)
            guardar_datos_csv(carga)
            guardar_datos_csv(bicicleta)
            guardar_datos_csv(motocicleta)

            #Impresión de datos
            print()
            print("\nLista de Vehiculos Particular")
            print(particular)
            print("\nLista de Vehiculos Carga")
            print(carga)
            print("\nLista de Vehiculos Bicicleta")
            print(bicicleta)
            print("\nLista de Vehiculos Motocicleta")
            print(motocicleta)
        case 4:
            print("\nSaliendo")
            False
            break
        case _:
            print("\nOpcion no valida")


