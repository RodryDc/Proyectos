from dataclasses import dataclass
from excepciones_personalizadas import ProductoNoEncontradoError, CantidadInsuficienteError, ErrorArchivoInventario

@dataclass
class Producto:
    codigo : int
    nombre : str
    precio : float
    cantidad : int

    def __str__(self):
        return f"El producto {self.nombre} con codigo: {self.codigo} tiene un precio de {self.precio} y su cantidad disponible es {self.cantidad}"
    
@dataclass
class Libro(Producto):
    autor : str
    editoria : str 

@dataclass
class Revista(Producto):
    numero_edicion : int
    fecha_publicacion : str

@dataclass
class Papeleria(Producto):
    pass

class Inventario():
    productos = []

    def agregar_producto(self,producto):
        self.productos.append(producto)

    def eliminar_producto(self,producto):
        self.productos.remove(producto)

    def modificar_producto(self,producto):
        pass

    def registrar_venta(self,codigo,cantidad):
        pass

    def guardar_inventario(self,archivo):
        print(archivo)
        with open(archivo,"w") as inventario:
            inventario.write(libro)
        raise ErrorArchivoInventario()

    def cargar_inventario(self,archivo):
        print(archivo)
        try:
            with open(archivo,"r") as inventario:
                print(inventario.read())
        except FileNotFoundError:            
            print("Error en el archivo, no exite")
            raise ErrorArchivoInventario("Error al cargar o guardar el archivo")

        

    class Venta(Libro,Revista,Papeleria):
        producto : Producto
        cantidad : int

        def calcular_total(self,precio_producto,cantidad):
            return precio_producto * cantidad


#Guardar y Cargar Inventario

inventario = Inventario()
inventario.cargar_inventario("inventario.txt")
# Agregar un producto
libro = Libro(codigo=101, nombre="Python para Todos", precio=15.99, cantidad=10,
autor="Juan Pérez", editorial="TechBooks")
inventario.agregar_producto(libro)
# Guardar el inventario en un archivo
inventario.guardar_inventario("inventario.txt")

#Registrar Venta
try:
    inventario = Inventario()
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