class Libro:
    def __init__(self,id,nombre,autor):
        self.__id = id
        self.__nombre = nombre
        self.__autor = autor
        self.__disponible = True

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        else:
            print("El libro ya se encuentra prestado")
            return False

    def devolver(self):        
        if not self.__disponible:
            self.__disponible = True
            return True
        else:
            print("El libro ya se encuentra devuelto")
            return False

    def esta_disponible(self):
        return self.__disponible
    
class Prestamo:
    def __init__(self):
        self.usuario = ""
        self.libro = ""
        self.fecha_prestamo = ""
        
    def generar_prestamo(self,usuario,libro,fecha_prestamo):
        if libro.esta_disponible():
            libro.prestar()
            self.usuario = usuario
            self.libro = libro
            self.fecha_prestamo = fecha_prestamo
            print("Prestamo generado")
        else:
            print("No se puede generar el prestamo")

class Usuario:
    def __init__(self,id,nombre):
        self.__id = id
        self.__nombre = nombre
        self.libro = []

    def mostrar_libros(self):
        if len(self.libro) == 0:
            print("No tiene libros")
        else:
            for i in self.libro:
                print(i)

    def solicitar_prestamo(self,libro,fecha_prestamo):
        prestamo = Prestamo()
        prestamo.generar_prestamo(self,libro,fecha_prestamo)

    def devolver_libro(self,libro):
        libro.devolver()
        self.libro.remove(libro)