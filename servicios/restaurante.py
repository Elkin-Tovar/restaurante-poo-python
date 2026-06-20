class Restaurante:

    def __init__(self):
        self.productos = []
        self.clientes = []

    #Métodos de la clase Restaurante
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\nProductos:")
        for p in self.productos:
            print(p)

    def mostrar_clientes(self):
        print("\nClientes:")
        for c in self.clientes:
            print(c)