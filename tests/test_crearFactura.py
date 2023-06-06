import sys
# Agregar la ruta del proyecto a la lista de rutas de búsqueda de módulos de Python
sys.path.append('/Users/isabellarivera/Desktop/proyecto CRUD')
# Python buscará los módulos en el directorio '/Users/isabellarivera/Desktop/proyecto CRUD'
# en caso de que no los encuentre en las rutas de búsqueda habituales.

import unittest
from datetime import datetime
from modelo.Cliente import Cliente
from modelo.Producto import Producto
from modelo.Factura import Factura
from CRUD.factura import crear_factura
from modelo.Plagas import ControlPlagas
from modelo.Fertilizantes import ControlFertilizantes
from modelo.Antibiotico import Antibiotico

class TestCrearFactura(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente(nombre="Isabella", cedula="1004737828", fecha_pedido="23052023")
        self.productos = [
            ControlPlagas(nombre="Plaga 1", frecuencia_aplicacion="Mensual", valor=100, periodo_carencia=10),
            ControlFertilizantes(nombre="Fertilizante 1", frecuencia_aplicacion="Anual", valor=200, fecha_ultima_aplicacion="Hace 3 dias"),
            Antibiotico(nombre="Antibiotico 1", dosis=1, tipo_animal="Bovino", precio=300, dosis_recomendada=2),
        ]

    def test_crear_factura(self):
        # Llamamos a la función para crear una factura
        crear_factura(self.cliente, self.productos)

        # Verificamos que el valor total de la compra sea el esperado
        self.assertEqual(sum([producto.valor for producto in self.productos]), self.cliente.facturas[0].total)

        # Verificamos que los productos agregados a la factura sean los esperados
        self.assertEqual([producto.nombre for producto in self.productos], [producto.nombre for producto in self.cliente.facturas[0].productos])

        # Verificamos que la fecha de compra de la factura sea la actual
        self.assertEqual(datetime.now().date(), self.cliente.facturas[0].fecha_compra.date())

if __name__ == "__main__":
    unittest.main()




