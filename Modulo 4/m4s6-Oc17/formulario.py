from dataclasses import dataclass

@dataclass
class Formulario:
    nombre: str
    correo: str
    productos: str
    nro_tarjeta: str

    def __post_init__(self):        
        if not self.nombre or not self.correo or not self.productos or not self.nro_tarjeta:
            raise ValueError("Todos los campos son obligatorios")
        if not self.nro_tarjeta.isnumeric():
            raise ValueError("El nro de tarjeta debe ser un entero")
        
    def enviar(self):
        print("Formulario enviado con exito")