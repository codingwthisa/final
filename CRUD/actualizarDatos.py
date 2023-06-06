from prettytable import PrettyTable
from ui.menu_actualizar import mostrar_menu_actualizar

def actualizar_factura(clientes):
    print("Lista de clientes:")
    table = PrettyTable()
    table.field_names = ["Nombre", "Cédula"]
    for cliente in clientes:
        table.add_row([cliente.nombre, cliente.cedula])
    print(table)

    cedula = input("Ingrese la cédula del cliente que desea actualizar: ")

    cliente_encontrado = False
    for cliente in clientes:
        if cliente.cedula == cedula:
            cliente_encontrado = True

            opcion = mostrar_menu_actualizar(cliente)

            if opcion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
                cliente.nombre = nuevo_nombre
                print("Nombre del cliente actualizado exitosamente.")

            elif opcion == "2":
                nueva_cedula = input("Ingrese la nueva cédula del cliente: ")
                cliente.cedula = nueva_cedula
                print("Cédula del cliente actualizada exitosamente.")

            elif opcion == "3":
                nueva_fecha_pedido = input("Ingrese la nueva fecha del pedido (en formato ddmmyyyy): ")
                cliente.fecha_pedido = nueva_fecha_pedido
                print("Fecha del pedido actualizada exitosamente.")

            else:
                print("Opción inválida.")

    if not cliente_encontrado:
        print(f"No se encontró un cliente con la cédula {cedula}.")