#aqui se ejecutara todo el codigo


from trabajador import Trabajador
from salario_semanal import SalarioSemanal

def main():
    # Datos del trabajador
    nombres = input("Ingrese el nombre del trabajador: ")
    horas_trabajadas = float(input("Ingrese las horas trabajadas en la semana: "))
    valor_hora_normal = float(input("Ingrese el valor de la hora normal de trabajo: "))

    # Crear instancia del trabajador
    trabajador = Trabajador(nombres, horas_trabajadas, valor_hora_normal)

    # Crear instancia de salario semanal
    salario_semanal = SalarioSemanal(trabajador)

    # Mostrar los resultados
    salario_semanal.mostrar_salario()

if __name__ == "__main__":
    main()
