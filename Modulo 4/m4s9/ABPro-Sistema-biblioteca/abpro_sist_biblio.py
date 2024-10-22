from dataclasses import dataclass
from datetime import datetime
from estado_personalizado import LibroNoDisponibleError, LibroNoEncontradoError
@dataclass
class Usuario:
    __nombre: str
    __id: int 

    def getNombre(self):
        return self.__nombre
    
    def getId(self):
        return self.__id
    
    @staticmethod
    def validar_id(id):
        if id > 0:
            return True
        
    @classmethod
    def contarUsuarios(cls):
        return len(cls)
    
    def __str__(self):
        return f"El nombre del usuario es {self.__nombre} y su ID es {self.__id}"
    
    def __repr__(self):
        return f"Usuario(nombre={self.__nombre},id={self.__id})"
    
@dataclass
class Lector(Usuario):
    prestamos: list
    @property
    def librosPrestados(self):
        return len(self.prestamos)
    
    def tomarLibro(self,libro):
        self.__prestamos.append(libro)
        print(f"El lector {self.__nombre} ha tomado el libro {libro}")
    
    def devolverLibro(self,libro):
        try:
            self.__prestamos.remove(libro)
            print(f"El lector {self.__nombre} ha devuelto el libro {libro}")
        except ValueError:
            print("El libro no se encuentra prestado")
    
    def __str__(self):
        return f"El lector {self.__nombre} tiene {self.librosPrestados} libros prestados"
    
    def __repr__(self):
        return f"Lector({self.__nombre},{self.__id},{self.prestamos})"   
    
@dataclass
class Administrador(Usuario):
    catalogo_libros: list
    @staticmethod
    def agregarLibro(libro):
        Administrador.catalogo_libros.append(libro)
        print(f"El libro {libro} ha sido agregado al catalogo")

    @staticmethod
    def eliminarLIbro(libro):
        if libro in Administrador.catalogo_libros:
           Administrador.catalogo_libros.remove(libro)
           print(f"El libro {libro} ha sido eliminado del catalogo")
        else:
            print(f"El libro {libro} no se encuentra en el catalogo")
            
    @classmethod
    def contarLIbros(cls):
        return len(cls)

    def __str__(self):
        return f"El administrador {self.__nombre} tiene {len(self.catalogo_libros)} libros en el catalogo"
    
    def __repr__(self):
        return f"Administrador({self.__nombre},{self.__id},{self.catalogo_libros})"
@dataclass
class LectorAministrador(Lector,Administrador):
    def __str__(self):
        return f"El lector {self.__nombre} tiene {self.librosPrestados} libros prestados"

    def __repr__(self):
        return f"LectorAministrador({self.__nombre},{self.__id},{self.prestamos},{self.catalogo_libros})"

class Libro:
    contador_libros = 0
    def __init__(self,titulo,autor,cod_unico,estado):
        self.titulo = titulo
        self.autor = autor
        self.cod_unico = cod_unico  
        self.estado = "disponible" 
        Libro.contador_libros += 1

    def estado(self):
        return self.estado
    
    @estado.seter
    def estado(self,nuevo_estado):
        if nuevo_estado in ["disponible","prestado"]:
            self.estado = nuevo_estado
        else:
            raise ValueError("El estado debe ser 'disponible' o 'prestado'")
        
    def prestar(self):
        if self.estado == "disponible":
            self.estado = "prestado"
            print("El libro ha sido prestado")
            return True
        else:
            print("El libro ya se encuentra prestado")
            return False
    
    def devolver(self):
        if self.estado == "prestado":
            self.estado = "disponible"
            print("El libro ha sido devuelto")
            return True
        else:
            print("El libro ya se encuentra devuelto")
            return False
    
    @classmethod
    def contar_libros(cls):
        return cls.contador_libros
    
    def __str__(self):
        return f"El libro {self.titulo} fue escrito por {self.autor} y su Codigo unico es {self.cod_unico}"
    
    def __repr__(self):
        return f"Libro({self.titulo},{self.autor},{self.cod_unico},{self.estado})"
    
class Prestamo:
    def __init__(self,lector,libro,fecha_prestamo, fecha_devolucion):
        self.lector = lector
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion

    @property
    def fechaDevolucion(self):
        return self._fecha_devolucion
    
    @fechaDevolucion.setter
    def fechaDevolucion(self, nueva_fecha_devolucion):
        if nueva_fecha_devolucion < self.fecha_prestamo:
            raise ValueError("La fecha de devolucion no puede ser anterior a la de prestamo")
        self._fecha_devolucion = nueva_fecha_devolucion

    def registrarPrestamo(self):
        print("Pretamo registrado")

    def devolverLibro(self):
        if self.fechaDevolucion is None:
            self.fechaDevolucion = datetime.now()
            print(f"el libro {self.libro} ha sido devuelto por {self.lector} en la fecha {self.fechaDevolucion}")
        else:
            print(f"el libro {self.libro} ya ha sido devuelto")
    
    def __str__(self):
        return f"Prestamo: {self.libro}, Lector: {self.lector}, fecha de prestamo: {self.fecha_prestamo}, Fecha de devolucion: {self.fechaDevolucion}"
    
    def __repr__(self):
        return f"Prestamo: {self.libro}, Lector: {self.lector}, fecha de prestamo: {self.fecha_prestamo}, Fecha de devolucion: {self.fechaDevolucion}"
    
    def guardar_inventario(self,archivo):
        print(f"Guardando en: {archivo}")
        try:
            with open(archivo, "a") as inventario:
                inventario.write(self.__str__())
        except Exception as e:
            raise (f"Error al guardar el archivo: {e}")

    def cargar_inventario(self, archivo):
        print(f"Cargando desde: {archivo}")
        try:
            with open(archivo, "r") as inventario:
                print(inventario.read())
        except FileNotFoundError:
            print(f"El archivo '{archivo}' no existe. Creando un nuevo archivo.")
            with open(archivo, "w") as inventario:
                inventario.write("") 



    