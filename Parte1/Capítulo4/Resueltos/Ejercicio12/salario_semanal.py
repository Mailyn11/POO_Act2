# aqui se calcularan los datos del salario 



from trabajador import Trabajador

class SalarioSemanal:
    def __init__(self, trabajador):
        self.trabajador = trabajador

    def calcular_salario(self):
        horas_normales = min(self.trabajador.horas_trabajadas, 40)
        horas_extras = max(0, self.trabajador.horas_trabajadas - 40)

        salario_normal = horas_normales * self.trabajador.valor_hora_normal

        # Si hay horas extras, las primeras 8 se pagan al doble y el resto al triple
        if horas_extras > 8:
            horas_extras_dobles = 8
            horas_extras_triples = horas_extras - 8
        else:
            horas_extras_dobles = horas_extras
            horas_extras_triples = 0

        # Calculo de las horas extras
        salario_extras_dobles = horas_extras_dobles * (self.trabajador.valor_hora_normal * 2)
        salario_extras_triples = horas_extras_triples * (self.trabajador.valor_hora_normal * 3)

        # El salario total es la suma de los salarios normales y de las horas extras
        salario_total = salario_normal + salario_extras_dobles + salario_extras_triples
        return salario_total

    def mostrar_salario(self):
        salario_total = self.calcular_salario()
        print(f"{self.trabajador.nombres}")
        print(f"Salario Total (incluyendo horas extras): {salario_total}")
