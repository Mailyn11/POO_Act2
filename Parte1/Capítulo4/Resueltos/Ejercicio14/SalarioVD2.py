class SalarioVD2:
    def __init__(self, ventas, salario_base):
        self.ventas = ventas
        self.salario_base = salario_base

    def calcular_salario(self, porcentaje_ventas):
        # Calcular salario final para el vendedor 2
        salario = self.salario_base
        if self.ventas > porcentaje_ventas:
            salario += 0.2 * salario  # Aumento del 20% si las ventas son mayores que el porcentaje
        return salario