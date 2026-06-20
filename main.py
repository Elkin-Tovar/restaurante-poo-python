from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear objetos
producto1 = Producto("Hamburguesa", 5.50, "Plato fuerte", True)
producto2 = Producto("Cola", 1.50, "Bebida", True)

cliente1 = Cliente("Juan Pérez", "0999999999", "juan@gmail.com")
cliente2 = Cliente("Saul Gimenez", "0989373839", "sauln@gmail.com")

# Crear restaurante
restaurante = Restaurante()

# Agregar datos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
restaurante.mostrar_productos()
restaurante.mostrar_clientes()