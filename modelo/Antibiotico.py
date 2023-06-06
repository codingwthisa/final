from .Producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre, dosis, tipo_animal, precio, dosis_recomendada):
        super().__init__("Antibiótico", nombre, "", precio)
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.dosis_recomendada = dosis_recomendada

    def to_dict(self):
        return {
            "tipo": self.tipo,
            "nombre": self.nombre,
            "dosis": self.dosis,
            "tipo_animal": self.tipo_animal,
            "precio": self.precio,
            "dosis_recomendada": self.dosis_recomendada
        }




