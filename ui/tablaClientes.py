from modelo.Cliente import Cliente
from typing import List
from prettytable import PrettyTable

def mostrar_tabla(clientes: List[Cliente]) -> None:
    table = PrettyTable()
    table.field_names = ["Nombre", "Cédula"]
    for cliente in clientes:
        table.add_row([cliente.nombre, cliente.cedula])
    print(table)

    cedula_cliente = input("Ingrese la cédula del cliente del cual desea ver su historial de compras: ")
    return cedula_cliente
    
