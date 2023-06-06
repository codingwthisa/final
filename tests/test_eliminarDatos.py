import sys
# Agregar la ruta del proyecto a la lista de rutas de búsqueda de módulos de Python
sys.path.append('/Users/isabellarivera/Desktop/proyecto CRUD')
# Python buscará los módulos en el directorio '/Users/isabellarivera/Desktop/proyecto CRUD'
# en caso de que no los encuentre en las rutas de búsqueda habituales.
import unittest
from modelo.Cliente import Cliente
from CRUD.eliminarDatos import eliminar_cliente

class TestEliminarCliente(unittest.TestCase):

    def test_eliminar_cliente_existente(self):
        # Crear clientes de prueba
        cliente1 = Cliente(nombre="Laura", cedula="1234567", fecha_pedido="12052023")
        cliente2 = Cliente(nombre="Maria", cedula="7654321", fecha_pedido="15052023")
        clientes = [cliente1, cliente2]

        eliminar_cliente(clientes, "1234567")

        self.assertEqual(len(clientes), 1)
        self.assertEqual(clientes[0].cedula, "7654321")

if __name__ == "__main__":
    unittest.main()