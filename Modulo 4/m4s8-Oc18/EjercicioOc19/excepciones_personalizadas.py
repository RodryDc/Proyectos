class ProductoNoEncontradoError(Exception):
    def __init__(self, error):
        super().__init__("Producto no existe en el inventario")

class CantidadInsuficienteError(Exception):
    def __init__(self, error):
        super().__init__("No hay suficiente cantidad del producto en el inventario para realizar la venta")

class ErrorArchivoInventario(Exception):
    pass
    # def __init__(self, error):
        # super().__init__("Error al cargar o guardar el archivo")