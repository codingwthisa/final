import sys
from PyQt5.QtWidgets import QInputDialog, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit
from CRUD.Controlador import Controlador
from modelo.Cliente import Cliente
from modelo.Plagas import ControlPlagas
from modelo.Antibiotico import Antibiotico
from modelo.Fertilizantes import ControlFertilizantes

class MenuVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: #F5F5F5;")

        layout = QHBoxLayout()

        menu_widget = QWidget()
        menu_widget.setStyleSheet("background-color: #333333;")

        menu_layout = QVBoxLayout()
        menu_layout.setSpacing(10)
        menu_layout.setContentsMargins(0, 20, 0, 20)

        botones_menu = ["1. Agregar compra", "2. Mostrar factura", "3. Actualizar", "4. Eliminar"]

        self.botones = []
        for opcion in botones_menu:
            boton = QPushButton(opcion, self)
            boton.setStyleSheet(
                "color: black; background-color: #7FB3D5; font-family: 'Arial'; font-size: 14px; border-radius: 15px;")
            boton.setFixedWidth(150)
            boton.setFixedHeight(30)
            boton.clicked.connect(self.boton_clicado)
            menu_layout.addWidget(boton)
            self.botones.append(boton)

        menu_widget.setLayout(menu_layout)

        self.area_visualizacion = QTextEdit()
        self.area_visualizacion.setStyleSheet("background-color: white; color: black;")
        self.area_visualizacion.setReadOnly(True)

        layout.addWidget(menu_widget)
        layout.addWidget(self.area_visualizacion)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        self.setLayout(layout)

        # Crear una instancia del controlador
        self.controlador = Controlador()

    def boton_clicado(self):
        boton_clicado = self.sender()
        for boton in self.botones:
            if boton is boton_clicado:
                boton.setStyleSheet("color: white; background-color: #5EB8E8; border-radius: 15px;")
            else:
                boton.setStyleSheet("color: black; background-color: #7FB3D5; border-radius: 15px;")

        # Llamar a la función correspondiente en el controlador
        if boton_clicado.text() == "1. Agregar compra":
            tipo_producto = self.mostrar_pregunta_tipo_producto()
            if tipo_producto == "Control de plagas":
                productos = self.mostrar_preguntas_control_plagas()
            elif tipo_producto == "Control Fertilizantes":
                productos = self.mostrar_preguntas_control_fertilizantes()
            elif tipo_producto == "Antibiótico":
                productos = self.mostrar_preguntas_antibiotico()
            else:
                productos = []  # Valor por defecto si no se cumple ninguna condición
                cliente = self.mostrar_preguntas_cliente()
                self.controlador.crear_factura(cliente, productos)
        elif boton_clicado.text() == "2. Mostrar factura":
            clientes = self.mostrar_preguntas_sistema_facturacion()
            self.controlador.crear_sistema_facturacion(clientes)
        elif boton_clicado.text() == "3. Actualizar":
            clientes = self.mostrar_preguntas_sistema_facturacion()
            self.controlador.actualizar_factura(clientes)
        elif boton_clicado.text() == "4. Eliminar":
            clientes = self.mostrar_preguntas_sistema_facturacion()
            cedula = self.mostrar_pregunta_cedula()
            self.controlador.eliminar_cliente(clientes, cedula)

    def mostrar_pregunta_tipo_producto(self):
        # Mostrar la pregunta y capturar la respuesta para el tipo de producto
        tipos_productos = ["Control de plagas", "Control Fertilizantes", "Antibiótico"]
        tipo_producto, ok = QInputDialog.getItem(self, "Agregar Producto", "Seleccione el tipo de producto:", tipos_productos)
        if ok:
            return tipo_producto

        return None

    def mostrar_preguntas_control_plagas(self):
        # Mostrar las preguntas y capturar las respuestas para el producto de control de plagas
        productos = []

        nombre, ok = QInputDialog.getText(self, "Agregar Producto", "Ingrese el nombre del producto:")
        if ok:
            frecuencia_aplicacion, ok = QInputDialog.getText(self, "Agregar Producto", "Ingrese la frecuencia de aplicación del producto:")
            if ok:
                valor, ok = QInputDialog.getDouble(self, "Agregar Producto", "Ingrese el precio del producto:")
                if ok:
                    periodo_carencia, ok = QInputDialog.getText(self, "Agregar Producto", "Ingrese el periodo de carencia del producto:")
                    if ok:
                        # Crear instancia del producto y agregarlo a la lista de productos
                        producto = ControlPlagas(nombre, frecuencia_aplicacion, valor, periodo_carencia)
                        productos.append(producto)

        return productos

    def mostrar_preguntas_control_fertilizantes(self):
        # Mostrar las preguntas y capturar las respuestas para el producto de control de plagas
        productos = []

        nombre, ok = QInputDialog.getText(self, "Agregar Producto", "Ingrese el nombre del producto:")
        if ok:
            frecuencia_aplicacion, ok = QInputDialog.getText(self, "Agregar Producto", "Ingrese la frecuencia de aplicación del producto:")
            if ok:
                valor, ok = QInputDialog.getDouble(self, "Agregar Producto", "Ingrese el precio del producto:")
                if ok:
                    fecha_ultima_aplicacion, ok = QInputDialog.getText(self, "Agregar Producto", "Ingrese la fecha de la última aplicación del producto: ")
                    if ok:
                        # Crear instancia del producto y agregarlo a la lista de productos
                        producto = ControlFertilizantes(nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion)

                        productos.append(producto)

        return productos

    def mostrar_preguntas_antibiotico(self):
        # Mostrar las preguntas y capturar las respuestas para el producto de antibiótico
        productos = []

        nombre, ok = QInputDialog.getText(self, "Agregar Producto", "Ingrese el nombre del antibiótico:")
        if ok:
            while True:
                try:
                    dosis, ok = QInputDialog.getInt(self, "Agregar Producto",
                                                    "Ingrese la dosis del antibiótico (entre 400 y 600 Kg):")
                    if ok and (dosis >= 400 and dosis <= 600):
                        break
                    else:
                        print("Dosis inválida. Intente de nuevo.")
                except ValueError:
                    print("Dosis inválida. Intente de nuevo.")

            opciones_tipo_animal = ["Bovinos", "Caprinos", "Porcinos"]
            tipo_animal, ok = QInputDialog.getItem(self, "Agregar Producto",
                                                   "Seleccione el tipo de animal al que se le puede aplicar el antibiótico:",
                                                   opciones_tipo_animal)
            if ok:
                valor, ok = QInputDialog.getDouble(self, "Agregar Producto", "Ingrese el precio del antibiótico:")
                if ok:
                    dosis_recomendada, ok = QInputDialog.getText(self, "Agregar Producto",
                                                                 "Ingrese la dosis recomendada del antibiótico:")
                    if ok:
                        # Crear instancia del producto y agregarlo a la lista de productos
                        producto = Antibiotico(nombre, dosis, tipo_animal, valor, dosis_recomendada)
                        productos.append(producto)

        return productos

    def mostrar_preguntas_cliente(self):
        # Mostrar las preguntas y capturar las respuestas para el cliente
        nombre, ok = QInputDialog.getText(self, "Agregar Cliente", "Ingrese el nombre del cliente:")
        if ok:
            cedula, ok = QInputDialog.getText(self, "Agregar Cliente", "Ingrese la cédula del cliente:")
            if ok:
                fecha_pedido, ok = QInputDialog.getText(self, "Agregar Cliente", "Ingrese la fecha del pedido (en formato ddmmyyyy):")
                if ok:
                    # Crear instancia del cliente y retornarlo
                    cliente = Cliente(nombre, cedula, fecha_pedido)
                    return cliente

        return None


    def mostrar_pregunta_cedula(self):
        # Mostrar la pregunta y capturar la respuesta para la cédula del cliente a eliminar
        cedula, ok = QInputDialog.getText(self, "Eliminar Cliente", "Ingrese la cédula del cliente a eliminar:")
        if ok:
            return cedula

        return None


app = QApplication(sys.argv)
ventana = MenuVentana()
ventana.setStyleSheet("background-color: #333333;")
ventana.showMaximized()
sys.exit(app.exec_())













