class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self,producto):
        self.productos.append(producto)
    
    def mostrar_pedido(self):
        print("Detalle del pedido:")
        total = 0
        for producto in self.productos:
            print(f"Producto {producto.nombre}, precio {producto.precio}")
            total += producto.precio
        print(f"Total = {total}")

class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        #self.pedidos = [] #Componentes: Pedidos que componen a Cliente. Es decir, si la instancia del cliente se elimina, todos sus pedidos también.
    
    def hacer_pedido(self,productos): #Puede ser un producto o una lista de productos
        pedido = Pedido() #Instanciación temporal de la clase Pedido, para la colaboración con Cliente
        for producto in productos:
            pedido.agregar_producto(producto)
        #self.pedidos.append(pedido) #Composición. Acá se agrega el pedido como un componente de Cliente
        print(f"El pedido de {self.nombre} fue realizado correctamente.")
        pedido.mostrar_pedido()

#Creación de productos predeterminados (inventario)
galletas = Producto("Triton",1000)
jugo = Producto("Zuko", 500)
bebida1 = Producto("Bilz",1500)
bebida2 = Producto("Pap",1500)

#Ejecución del programa
print("Bienvenido a aCuenta")
nombre = input("Ingresa tu nombre")
cliente = Cliente(nombre) #Instanciación del cliente

cliente.hacer_pedido([galletas,jugo]) #Realización del pedido de ese cliente


