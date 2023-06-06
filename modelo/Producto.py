class Producto:
    def __init__(self, tipo, nombre, frecuencia_aplicacion, valor):
        self.tipo = tipo
        self.nombre = nombre
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.valor = valor

    def calcular_precio(self):
        return int(self.valor)


