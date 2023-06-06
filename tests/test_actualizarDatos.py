import sys
# Agregar la ruta del proyecto a la lista de rutas de búsqueda de módulos de Python
sys.path.append('/Users/isabellarivera/Desktop/proyecto CRUD')
# Python buscará los módulos en el directorio '/Users/isabellarivera/Desktop/proyecto CRUD'
# en caso de que no los encuentre en las rutas de búsqueda habituales.

import unittest
from modelo.Cliente import Cliente
from CRUD.actualizarDatos import actualizar_factura
from unittest.mock import patch

class TestActualizarFactura(unittest.TestCase):
    
    def test_actualizar_factura(self):
        cliente = Cliente("Juan", "1111", "20210510")
        clientes = [cliente]
        with patch('builtins.input', side_effect=['1111','3', '14052023']):
            actualizar_factura(clientes)
        self.assertEqual(cliente.fecha_pedido, '14052023')


if __name__ == "__main__":
    unittest.main()
