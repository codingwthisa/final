from datetime import datetime
from typing import List
from prettytable import PrettyTable
from modelo.Cliente import Cliente
from modelo.Producto import Producto
from modelo.Factura import Factura

def crear_factura(cliente: Cliente, productos: List[Producto]) -> None:
    table = PrettyTable()
    table.field_names = ["Producto", "Tipo", "Cliente", "Cédula", "Fecha de la compra", "Total"]

    for producto in productos:
        table.add_row([producto.nombre, producto.__class__.__name__, cliente.nombre, cliente.cedula, cliente.fecha_pedido, producto.valor])
    
    print(table)
    print(f"Valor total de la compra: {sum([producto.valor for producto in productos])}")

    factura = Factura(cliente, elementos_facturados=[], productos=[], fecha_compra=datetime.now())
    for producto in productos:
        factura.agregar_producto(producto)

    cliente.agregar_factura(factura)



