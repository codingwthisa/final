from datetime import datetime
from typing import List
from .Producto import Producto

class Factura:
    def __init__(self, cliente, elementos_facturados, productos: List[Producto], fecha_compra=datetime.now()):
        self.cliente = cliente
        self.elementos_facturados = elementos_facturados
        self.fecha_compra = fecha_compra
        self.productos = productos
        self.total = self.calcular_total_factura()

    def calcular_total_factura(self):
        total = 0
        for elemento in self.productos:
            total += elemento.calcular_precio()
        return total

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total = self.calcular_total_factura()

    def from_string(cls, factura_str):
        cliente, elementos_str, fecha_str = factura_str.split(',')
        elementos_facturados = [int(x) for x in elementos_str.split(';')]
        fecha_compra = datetime.strptime(fecha_str.strip(), '%Y-%m-%d %H:%M:%S.%f')
        return cls(cliente, elementos_facturados, [], fecha_compra)











