from dataclasses import dataclass
from excepciones_personalizadas import ProductoNoEncontradoError, CantidadInsuficienteError, ErrorArchivoInventario

@dataclass
class Producto:
    codigo : int
    nombre : str
    precio : float
    cantidad : int

    def __str__(self):
        return f"El producto {self.nombre} con codigo: {self.codigo} tiene un precio de {self.precio} y su cantidad disponible es {self.cantidad} \n"
    
@dataclass
class Libro(Producto):
    autor : str
    editorial : str 

@dataclass
class Revista(Producto):
    numero_edicion : int
    fecha_publicacion : str

@dataclass
class Papeleria(Producto):
    pass

class Inventario():
    def __init__(self):
        self.productos = []

    def __str__(self):
        return "\n".join([str(producto) for producto in self.productos])

    def agregar_producto(self,producto):
        self.productos.append(producto)

    def eliminar_producto(self,producto):
        self.productos.remove(producto)

    def modificar_producto(self, codigo, nombre=None, precio=None, cantidad=None):
        for producto in self.productos:
            if producto.codigo == codigo:
                if nombre:
                    producto.nombre = nombre
                if precio:
                    producto.precio = precio
                if cantidad:
                    producto.cantidad = cantidad
                return
        raise ProductoNoEncontradoError(f"El producto con código {codigo} no fue encontrado.")


    def registrar_venta(self,codigo,cantidad):
        for producto in self.productos:
            if producto.codigo == codigo:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    print(f"Venta realizada. Se vendieron {cantidad} unidades de {producto.nombre}.")
                    return
                else:
                    raise CantidadInsuficienteError(f"No hay suficiente cantidad de {producto.nombre} para la venta.")
        raise ProductoNoEncontradoError(f"El producto con código {codigo} no fue encontrado.")


    def guardar_inventario(self,archivo):
        print(f"Guardando en: {archivo}")
        try:
            with open(archivo, "a") as inventario:
                inventario.write(self.__str__())
        except Exception as e:
            raise ErrorArchivoInventario(f"Error al guardar el archivo: {e}")

    def cargar_inventario(self, archivo):
        print(f"Cargando desde: {archivo}")
        try:
            with open(archivo, "r") as inventario:
                print(inventario.read())
        except FileNotFoundError:
            print(f"El archivo '{archivo}' no existe. Creando un nuevo archivo.")
            with open(archivo, "w") as inventario:
                inventario.write("") 
        
    @dataclass
    class Venta(Libro,Revista,Papeleria):
        producto : Producto
        cantidad : int

        def calcular_total(self):
            return self.producto.precio * self.cantidad


#Guardar y Cargar Inventario

inventario = Inventario()
inventario.cargar_inventario("inventario.txt")
#Agregar un producto
libro = Libro(codigo=101, nombre="Python para Todos", precio=15.99, cantidad=10, autor="Juan Pérez", editorial="TechBooks")
inventario.agregar_producto(libro)
# Guardar el inventario en un archivo
inventario.guardar_inventario("inventario.txt")

#Registrar Venta
try:
    #inventario = Inventario()
    inventario.cargar_inventario("inventario.txt")
    # Registrar una venta
    inventario.registrar_venta(101, 2)
    # Vender 2 unidades del producto con código 101
    # Guardar cambios en el inventario
    inventario.guardar_inventario("inventario.txt")
except ProductoNoEncontradoError as e:
    print(f"Error: {e}")
except CantidadInsuficienteError as e:
    print(f"Error: {e}")
except ErrorArchivoInventario as e:
    print(f"Error al manejar el archivo del inventario: {e}")