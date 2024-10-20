class Inventario:
    def __init__(self):
        self.productos = []

    def __str__(self):
        return "\n".join([str(producto) for producto in self.productos])

    def guardar_inventario(self, archivo):
        print(f"Guardando en: {archivo}")
        try:
            with open(archivo, "w") as inventario:
                inventario.write(self.__str__())
        except Exception as e:
            raise ErrorArchivoInventario(f"Error al guardar el archivo: {e}")

    def cargar_inventario(self, archivo):
        print(f"Cargando desde: {archivo}")
        try:
            with open(archivo, "r") as inventario:
                contenido = inventario.read()
                print(contenido)
        except FileNotFoundError:
            print(f"El archivo '{archivo}' no existe. Creando un nuevo archivo.")
            with open(archivo, "w") as inventario:
                inventario.write("")  # Crear un archivo vacío si no existe

# Guardar y Cargar Inventario
inventario = Inventario()
inventario.cargar_inventario("inventario.txt")
