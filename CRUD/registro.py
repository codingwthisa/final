from modelo.Antibiotico import Antibiotico
from modelo.Cliente import Cliente
from modelo.Plagas import ControlPlagas
from modelo.Fertilizantes import ControlFertilizantes
from ui.menu_registro import mostrar_menu_registro
from .factura import crear_factura
from typing import List

productos_control_plagas, productos_control_fertilizantes, productos_antibioticos = [], [], []

def crear_sistema_facturacion(clientes: List[Cliente] = []) -> tuple:

    productos_control = []
    antibioticos = []
 
    while True:

        opcion = mostrar_menu_registro()

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación del producto: ")
            valor = float(input("Ingrese el precio del producto: "))
            periodo_carencia = input("Ingrese el periodo de carencia del producto: ")

            producto = ControlPlagas(nombre, frecuencia_aplicacion, valor, periodo_carencia)

            productos_control.append(producto)

        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ")
            frecuencia_aplicacion = input("Ingrese la frecuencia de aplicación del producto: ")
            valor = float(input("Ingrese el precio del producto: "))
            fecha_ultima_aplicacion = input("Ingrese la fecha de la última aplicación del producto: ")

            producto = ControlFertilizantes(nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion)
            
            productos_control.append(producto)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del antibiótico: ")
            while True:
                try:
                    dosis = int(input("Ingrese la dosis del antibiótico (entre 400 y 600 Kg): "))
                    if dosis < 400 or dosis > 600:
                        raise ValueError
                    break
                except ValueError:
                    print("Dosis inválida. Intente de nuevo.")

            tipo_animal = ""
            while tipo_animal not in ["Bovinos", "Caprinos", "Porcinos"]:
                print("Seleccione el tipo de animal al que se le puede aplicar el antibiótico:")
                print("1. Bovinos")
                print("2. Caprinos")
                print("3. Porcinos")
                opcion = input("Ingrese el número correspondiente a la opción: ")
                if opcion == "1":
                    tipo_animal = "Bovinos"
                elif opcion == "2":
                    tipo_animal = "Caprinos"
                elif opcion == "3":
                    tipo_animal = "Porcinos"
                else:
                    print("Opción inválida. Intente de nuevo.")

            valor = float(input("Ingrese el precio del antibiótico: "))
            dosis_recomendada = input("Ingrese la dosis recomendada del antibiótico: ")

            producto = Antibiotico(nombre, dosis, tipo_animal, valor, dosis_recomendada)

            antibioticos.append(producto)

        elif opcion == "4":
            break

    while True:
        nombre = input("Ingrese el nombre del cliente: ")
        cedula = input("Ingrese la cédula del cliente: ")
        fecha_pedido = input("Ingrese la fecha del pedido (en formato ddmmyyyy): ")

        cliente = Cliente(nombre, cedula, fecha_pedido)
        clientes.append(cliente)

        otra_compra = input("¿El cliente realizó otra compra? (S/N): ")
        if otra_compra.upper() == "N":
            break

    return productos_control, antibioticos, clientes

if __name__ == '__main__':
    productos_control, antibioticos, clientes = crear_sistema_facturacion()
    productos = productos_control + antibioticos 
    crear_factura(clientes[-1], productos)



  





