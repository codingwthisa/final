class Cliente:
    def __init__(self, nombre, cedula, fecha_pedido):
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_pedido = fecha_pedido
        self.facturas = []

    def agregar_factura(self, factura):
        self.facturas.append(factura)
        total_factura = factura.calcular_total_factura()
        self.facturas[-1].total_factura = total_factura

    



