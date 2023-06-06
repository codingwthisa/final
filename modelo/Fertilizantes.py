from .Plagas import Producto

class ControlFertilizantes(Producto):
    def __init__(self, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
        super().__init__("Control de Fertilizantes", nombre, frecuencia_aplicacion, valor)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

