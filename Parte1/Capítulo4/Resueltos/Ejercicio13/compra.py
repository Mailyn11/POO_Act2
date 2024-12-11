#aqui se alacenaran datos de la compra


class Compra:
    def __init__(self, valor_compra, color_bolita):
        self.valor_compra = valor_compra
        self.color_bolita = color_bolita.lower()  # Convertimos el color a minúsculas para evitar errores de comparación

    def calcular_descuento(self):
        if self.color_bolita == "blanca":
            descuento = 0
        elif self.color_bolita == "verde":
            descuento = 0.10
        elif self.color_bolita == "amarilla":
            descuento = 0.25
        elif self.color_bolita == "azul":
            descuento = 0.50
        elif self.color_bolita == "roja":
            descuento = 1.00
        else:
            descuento = 0
            print("Color de bolita no válido. Asumiendo sin descuento.")
        
        return descuento

    def calcular_total(self):
        descuento = self.calcular_descuento()
        total = self.valor_compra * (1 - descuento)
        return total

    def mostrar_total(self):
        total = self.calcular_total()
        print(f"Compra Total: {self.valor_compra}")
        print(f"Descuento Aplicado: {self.calcular_descuento() * 100}%")
        print(f"Total a Pagar: {total:.2f}")
