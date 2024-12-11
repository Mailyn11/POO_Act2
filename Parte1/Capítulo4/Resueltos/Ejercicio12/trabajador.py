#aqui almacenaremos los datos del trabajador


class Trabajador:
    def __init__(self, nombres, horas_trabajadas, valor_hora_normal):
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora_normal = valor_hora_normal

    def __str__(self):
        return f"Nombre: {self.nombres}, Horas trabajadas: {self.horas_trabajadas}, Valor hora normal: {self.valor_hora_normal}"
