from abc import ABC, abstractmethod
from modelo.Cliente import Cliente
from typing import List
from modelo.Producto import Producto


class ICRUD(ABC):

    @abstractmethod
    def actualizar_factura(self, clientes):
        pass

    @abstractmethod
    def buscar_por_cedula(self, clientes: List[Cliente]) -> None:
        pass

    @abstractmethod
    def eliminar_cliente(self, clientes, cedula):
        pass

    @abstractmethod
    def crear_factura(self, cliente: Cliente, productos: List[Producto]) -> None:
        pass

    @abstractmethod
    def crear_sistema_facturacion(self, clientes: List[Cliente] = []) -> tuple:
        pass
