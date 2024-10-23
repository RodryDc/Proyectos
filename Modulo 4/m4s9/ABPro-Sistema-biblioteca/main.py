from abpro_sist_biblio import Administrador, Lector, Prestamo, Libro
from estado_personalizado import LibroNoDisponibleError, LibroNoEncontradoError

prestamos = []
lectores = []
libros = []
administrador = None

while True:
    print("\n=== Menú de Biblioteca ===")
    print("1. Crear Administrador")
    print("2. Crear Lector")
    print("3. Agregar Libro al catálogo (Administrador)")
    print("4. Eliminar Libro del catálogo (Administrador)")
    print("5. Prestar Libro a Lector")
    print("6. Devolver Libro por Lector")
    print("7. Mostrar Lector")
    print("8. Mostrar Administrador")
    print("9. Guardar Libros en archivo")
    print("10. Cargar Libros desde archivo")
    print("11. Guardar Usuarios en archivo")
    print("12. Cargar Usuarios desde archivo")
    print("13. Mostrar Préstamos")
    print("14. Salir")
    
    opcion = input("Selecciona una opción: ")

    try:
        if opcion == "1":
            nombre = input("Introduce el nombre del administrador: ")
            id_administrador = int(input("Introduce el ID del administrador: "))
            administrador = Administrador(nombre, id_administrador, [])
            print(f"Administrador {nombre} creado.")

        elif opcion == "2":
            nombre = input("Introduce el nombre del lector: ")
            id_lector = int(input("Introduce el ID del lector: "))
            lector = Lector(nombre, id_lector, [])
            lectores.append(lector)
            print(f"Lector {nombre} creado.")

        elif opcion == "3":
            if administrador:
                titulo = input("Introduce el título del libro: ")
                autor = input("Introduce el autor del libro: ")
                cod_unico = input("Introduce el código único del libro: ")
                libro = Libro(titulo, autor, cod_unico, "disponible")
                administrador.agregarLibro(libro)
                libros.append(libro) 
            else:
                raise ValueError("Primero debes crear un Administrador.")
        
        elif opcion == "4":
            if administrador:
                titulo = input("Introduce el título del libro a eliminar: ")
                libro_a_eliminar = next((libro for libro in libros if libro.titulo == titulo), None)
                if libro_a_eliminar:
                    administrador.eliminarLibro(libro_a_eliminar)  # Cambia aquí
                    libros.remove(libro_a_eliminar)
                    print(f"El libro {titulo} ha sido eliminado del catálogo.")
                else:
                    print("El libro no se encuentra en el catálogo.")
            else:
                print("Primero debes crear un Administrador.")
    
        elif opcion == "5":  # Prestar libro a lector
            if len(lectores) > 0 and len(libros) > 0:
                id_lector = int(input("Introduce el ID del lector: "))
                lector = None
                for l in lectores:
                    if l.getId() == id_lector:
                        lector = l
                        break

                titulo_libro = input("Introduce el título del libro a prestar: ")
                libro = None
                for l in libros:
                    if l.titulo == titulo_libro and l.estado == "disponible":
                        libro = l
                        break

                if lector and libro:
                    prestamo = Prestamo(lector, libro)
                    prestamos.append(prestamo)
                    lector.tomarLibro(libro)
                    libro.prestar()
                    prestamo.registrarPrestamo()
                else:
                    raise LibroNoDisponibleError(f"El libro {titulo_libro} no está disponible o no se encontró el lector.")
            else:
                raise ValueError("No hay lectores o libros registrados.")
        
        elif opcion == "6":
            id_lector = int(input("Introduce el ID del lector: "))
            lector = None
            for l in lectores:
                if l.getId() == id_lector:
                    lector = l
                    break

            titulo_libro = input("Introduce el título del libro a devolver: ")
            libro = None
            for l in libros:
                if l.titulo == titulo_libro:
                    libro = l
                    break

            if lector and libro:
                lector.devolverLibro(libro)
                libro.devolver()
            else:
                raise ValueError("Lector o libro no encontrados.")

        elif opcion == "7":
            id_lector = int(input("Introduce el ID del lector: "))
            lector = None
            for l in lectores:
                if l.getId() == id_lector:
                    lector = l
                    break
            if lector:
                print(lector)
            else:
                raise ValueError(f"Lector con ID {id_lector} no encontrado.")

        elif opcion == "8":
            if administrador:
                print(administrador)
            else:
                raise ValueError("Primero debes crear un Administrador.")
        
        elif opcion == "9":
            archivo_libros = input("Introduce el nombre del archivo para guardar los libros: ")
            Prestamo.guardar_libros(archivo_libros, libros)

        elif opcion == "10":
            archivo_libros = input("Introduce el nombre del archivo para cargar los libros: ")
            libros = Prestamo.cargar_libros(archivo_libros)

        elif opcion == "11":
            archivo_usuarios = input("Introduce el nombre del archivo para guardar los usuarios: ")
            Prestamo.guardar_usuarios(archivo_usuarios, lectores + [administrador] if administrador else lectores)

        elif opcion == "12":
            archivo_usuarios = input("Introduce el nombre del archivo para cargar los usuarios: ")
            usuarios = Prestamo.cargar_usuarios(archivo_usuarios)
            lectores = [u for u in usuarios if isinstance(u, Lector)]
            administrador = next((u for u in usuarios if isinstance(u, Administrador)), None)

        elif opcion == "13":
            if prestamos:
                for prestamo in prestamos:
                    print(prestamo)
            else:
                print("No hay préstamos registrados.")

        elif opcion == "14":
            print("Saliendo del sistema...")
            break

        else:
            raise ValueError("Opción no válida, intenta de nuevo.")
    
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except LibroNoDisponibleError as lnde:
        print(f"Error de disponibilidad: {lnde}")
    except LibroNoEncontradoError as lnee:
        print(f"Error: {lnee}")
    except Exception as e:
        print(f"Error inesperado: {e}")
