
from modelo.Producto import Producto
from modelo.Cliente import Cliente
from typing import List
from CRUD.ICRUD_interface import ICRUD
from CRUD.actualizarDatos import actualizar_factura
from CRUD.buscarCedula import buscar_por_cedula
from CRUD.eliminarDatos import eliminar_cliente
from CRUD.factura import crear_factura
from CRUD.registro import crear_sistema_facturacion

class Controlador(ICRUD):

    def actualizar_factura(self, clientes):
        return actualizar_factura(clientes)

    def buscar_por_cedula(self, clientes: List[Cliente]) -> None:
        return buscar_por_cedula(clientes)

    def eliminar_cliente(self, clientes, cedula):
        return eliminar_cliente(clientes, cedula)

    def crear_factura(self, cliente: Cliente, productos: List[Producto]) -> None:
        return crear_factura(cliente, productos)

    def crear_sistema_facturacion(self, clientes: List[Cliente] = []) -> tuple:
        return crear_sistema_facturacion(clientes)


