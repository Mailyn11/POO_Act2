#aqui se almacenan los datos del empleado

from salario import Salario

class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion_fuente):
        self.codigo = codigo
        self.nombres = nombres
        self.salario = Salario(horas_trabajadas, valor_hora, retencion_fuente)

    def mostrar_informacion(self):
        salario_bruto = self.salario.calcular_salario_bruto()
        salario_neto = self.salario.calcular_salario_neto()
        print(f"Código del empleado: {self.codigo}")
        print(f"Nombres: {self.nombres}")
        print(f"Salario bruto: ${salario_bruto:.2f}")
        print(f"Salario neto: ${salario_neto:.2f}")
