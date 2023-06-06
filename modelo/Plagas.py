from .Producto import Producto

class ControlPlagas(Producto):
    def __init__(self, nombre, frecuencia_aplicacion, valor, periodo_carencia):
        super().__init__("Control de Plagas", nombre, frecuencia_aplicacion, valor)
        self.periodo_carencia = periodo_carencia

    def calcular_precio(self):
        precio_final = self.valor
        return precio_final


