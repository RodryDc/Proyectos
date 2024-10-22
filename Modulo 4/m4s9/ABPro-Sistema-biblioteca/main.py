from abpro_sist_biblio import Administrador, Lector, LectorAministrador

while True:
    print("MENU")
    print("Selecciona el tipo de Usuario")
    print("1.-Administrador")
    print("2.- Lector")
    print("3.- Lector - Administrador")
    print("4.- salir")
    opcion = int(input("Ingresa tu opción"))

    match opcion:
        case 1: #Administrador
            print("Administrador")
            print("1. Agregar libros")
            print("2. Eliminar libros")
            print("3. Mostrar libros")
            print("4. Salir")
            while True:
                op = int(input("Ingresa tu opción"))
                match op:
                    case 1:
                        Administrador.agregarLibro()
                        break
                    case 2:
                        Administrador.eliminarLIbro()
                        break
                    case 3:
                        Administrador.__str__()
                        break
                    case 4:
                        False
                        break
                    case _:
                        print("Opcion incorrecta")
                        break
            break
        case 2: #Lector
            print("Lector")
            print("1. Tomar libro")
            print("2. Devolver libro")
            print("3. Mostrar libros")
            print("4. Salir")
            while True:
                op = int(input("Ingresa tu opción"))
                match op:
                    case 1:
                        Lector.tomarLibro()
                        break
                    case 2:
                        Lector.devolverLibro()
                        break
                    case 3:
                        Lector.__str__()
                        break
                    case 4:
                        False
                        break
                    case _:
                        print("Opcion incorrecta")
                        break
            break
        case 3: #Lector - Administrador
            print("Lector - Administrador")
            print("1. Tomar libro")
            print("2. Devolver libro")
            print("3. Mostrar libros")
            print("5. Agregar libros")
            print("6. Eliminar libros")
            print("4. Salir")
            while True:
                op = int(input("Ingresa tu aplicación"))
                match op:
                    case 1:
                        LectorAministrador.tomarLibro()
                        break
                    case 2:
                        LectorAministrador.devolverLibro()
                        break
                    case 3:
                        LectorAministrador.__str__()
                        break
                    case 4:
                        LectorAministrador.agregarLibro()
                        break
                    case 5:
                        LectorAministrador.eliminarLIbro()
                        break
                    case 6:
                        False
                        break
                    case _:
                        print("Opcion incorrecta")
                        break
            break
        case 4:
            False
            break
        case _:
            print("Opcion incorrecta")
            break
