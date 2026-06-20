#Crear la clase producto
class Producto:
    #Definir el metodo constructor e inicializar los atributos
    def __init__(self, nombre, precio, categoria, disponible):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.disponible = disponible
    
    #uso de __str__ para retornar la informacion de los objetos 
    def __str__(self):
        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Categoría: {self.categoria} | "
            f"Disponible: {'Si' if self.disponible else 'No'} | "
        )
    

