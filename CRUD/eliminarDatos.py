from prettytable import PrettyTable

def eliminar_cliente(clientes, cedula):
    for cliente in clientes:
        if cliente.cedula == cedula:
            clientes.remove(cliente)
            print(f"Cliente con cédula {cedula} eliminado exitosamente.")
            return
    print(f"No se encontró ningún cliente con cédula {cedula}.")
