#Crear la clase cliente 
class Cliente:
    #definir metodo constructor e inicializar os atributos  
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    #uso de __str__ para retornar la informacion de los objetos
    def __str__(self):
        return(
            f"Cliente: {self.nombre} | "
            f"Teléfono: {self.telefono} | "
            f"Correo: {self.correo} | "
        )

        