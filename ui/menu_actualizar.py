def mostrar_menu_actualizar(cliente):
    print(f"Cliente encontrado: {cliente.nombre}")
    print("¿Qué dato de la factura desea modificar?")
    print("1. Nombre del cliente")
    print("2. Cédula del cliente")
    print("3. Fecha del pedido")

    opcion = input("Seleccione una opción: ")
    return opcion
    
