class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio


class Pedido:
    def __init__(self):
        self.productos =[]

    def agregar_producto(self,producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Detalle del pedido: ")
        total = 0
        for producto in self.productos:
            print(f" Producto: {producto.nombre}: ${producto.precio}")
            total += producto.precio
        print(f"Total: ${total}")

class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.pedidos = [] # Lista de pedidos
    
    def hacer_pedido(self,productos):
        pedido = Pedido()
        for producto in productos:
            pedido.agregar_producto(producto)
        self.pedidos.append(pedido)
        print(f"El pedido de {self.nombre} ha sido procesado")
        pedido.mostrar_productos()

galletas = Producto("Triton", 1000)
jugo = Producto("Zuko", 500)
bebida1 = Producto("Bilz", 1500)
bebida2 = Producto("Pap", 1500)

print("Bienvenio a aCUENTA")
nombre = input("Ingresa tu nombre: ")
cliente = Cliente(nombre)

cliente.hacer_pedido([galletas, jugo])

# pedido1 = Pedido()
# pedido1.agregar_producto(galletas)
# pedido1.agregar_producto(jugo)

# print(pedido1.productos)
