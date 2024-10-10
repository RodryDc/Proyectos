"""ABP: Sistema de Biblioteca
Contexto
La Biblioteca Municipal "El Saber" ha decidido modernizar su sistema de préstamos de
libros, el cual hasta ahora se ha gestionado manualmente con fichas de papel. Esto ha
ocasionado problemas como la pérdida de fichas, dificultad para realizar seguimientos
a los préstamos, y la posibilidad de que un mismo libro sea prestado más de una vez al
mismo tiempo.
El director de la biblioteca ha solicitado desarrollar un sistema de software que
permita gestionar los libros disponibles, los usuarios que hacen uso de los servicios
y los préstamos de libros. El objetivo es mejorar la organización de la biblioteca y
evitar conflictos con el préstamo de ejemplares.
Objetivo:
El objetivo es desarrollar un programa orientado a objetos que permita:
Gestionar los préstamos y devoluciones de libros por parte de un usuario.
Asegurar que un libro no pueda ser prestado a más de una persona a la vez.
Mantener la privacidad de los datos sensibles de los usuarios
(encapsulamiento).
Permitir la colaboración entre distintas clases, como Libro , Usuario y
Prestamo .
Especificaciones del sistema:
1. Libros: Cada libro tiene un título, autor y un número de identificación único
(ID).
2. Usuarios: Cada usuario tiene un nombre y un número de identificación único. Los
usuarios deben poder solicitar préstamos y devolver libros.
3. Préstamos: Cada préstamo debe registrar qué usuario pidió un libro y en qué
fecha. No se debe permitir prestar un libro si ya está en préstamo.
4. Requerimientos funcionales:
El programa debe permitir crear nuevos libros y usuarios.
Debe asegurarse que los datos de los usuarios y libros estén
encapsulados, de manera que no puedan ser modificados directamente.
Permitir la devolución de libros.
Pasos para abordar el problema:
1. Análisis del problema:
Discute cómo representarías los libros, usuarios y préstamos.
¿Qué atributos y métodos deben tener las clases Libro , Usuario y
Prestamo ?
¿Cómo asegurarías que un libro no pueda ser prestado más de una vez
hasta que se devuelva?
2. Definición de clases y atributos:
Diseña las clases Libro , Usuario y Prestamo .
Define los atributos y métodos de cada clase, asegurándote de encapsular
los datos sensibles (como los detalles del libro y los datos del usuario).
3. Implementación:
Codifica las clases aplicando los conceptos de abstracción,
encapsulamiento y colaboración.
Asegúrate de que la clase Prestamo gestione las relaciones entre Libro
y Usuario .
4. Validación:
Asegúrate de que no sea posible prestar un libro que ya esté prestado.
Implementa la lógica para devolver libros y actualizar el estado del
préstamo."""

from datetime import datetime

class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.__id_libro = id_libro
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True  # El libro está disponible para préstamo inicialmente

    @property
    def id_libro(self):
        return self.__id_libro

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    def esta_disponible(self):
        return self.__disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__prestamos = []

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def nombre(self):
        return self.__nombre

    def agregar_prestamo(self, prestamo):
        self.__prestamos.append(prestamo)

    def remover_prestamo(self, prestamo):
        if prestamo in self.__prestamos:
            self.__prestamos.remove(prestamo)

    def obtener_prestamos(self):
        return self.__prestamos


class Prestamo:
    def __init__(self, usuario, libro):
        self.__usuario = usuario
        self.__libro = libro
        self.__fecha_prestamo = datetime.now()
        self.__activo = True

    @property
    def usuario(self):
        return self.__usuario

    @property
    def libro(self):
        return self.__libro

    @property
    def fecha_prestamo(self):
        return self.__fecha_prestamo

    def devolver_libro(self):
        if self.__activo:
            self.__activo = False
            self.__libro.devolver()
            self.__usuario.remover_prestamo(self)
            return True
        return False

    def es_activo(self):
        return self.__activo

# Crear una instancia de Libro y Usuario
libro1 = Libro(1, "Cien Años de Soledad", "Gabriel García Márquez")
usuario1 = Usuario(1, "Juan Pérez")

# Realizar el préstamo si el libro está disponible
if libro1.esta_disponible():
    prestamo1 = Prestamo(usuario1, libro1)
    libro1.prestar()
    usuario1.agregar_prestamo(prestamo1)
    print(f"El libro '{libro1.titulo}' ha sido prestado a {usuario1.nombre} en la fecha {prestamo1.fecha_prestamo}.")
else:
    print("El libro no está disponible para préstamo.")

# Crear otro usuario
usuario2 = Usuario(2, "Ana Gómez")

# Intentar prestar el mismo libro a otro usuario mientras aún está prestado
if libro1.esta_disponible():
    prestamo2 = Prestamo(usuario2, libro1)
    libro1.prestar()
    usuario2.agregar_prestamo(prestamo2)
    print(f"El libro '{libro1.titulo}' ha sido prestado a {usuario2.nombre}.")
else:
    print(f"El libro '{libro1.titulo}' ya está prestado y no se puede prestar de nuevo.")

# Devolver el libro prestado por el primer usuario
if prestamo1.devolver_libro():
    print(f"El libro '{libro1.titulo}' ha sido devuelto por {usuario1.nombre}.")
else:
    print("No fue posible devolver el libro.")

# Verificar disponibilidad después de la devolución
if libro1.esta_disponible():
    print(f"El libro '{libro1.titulo}' está disponible para otro préstamo.")
else:
    print(f"El libro '{libro1.titulo}' no está disponible.")