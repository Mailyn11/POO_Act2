#este es el codigo principal

from empleado import Empleado

# Bloque principal
def main():
    # Solicitar información del empleado
    codigo = input("Ingrese el código del empleado: ")
    nombres = input("Ingrese los nombres del empleado: ")
    horas_trabajadas = float(input("Ingrese el número de horas trabajadas al mes: "))
    valor_hora = float(input("Ingrese el valor por hora trabajada: "))
    retencion_fuente = float(input("Ingrese el porcentaje de retención en la fuente: "))

    # Crear instancia de la clase Empleado
    empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, retencion_fuente)

    # Mostrar información del empleado
    print("\nInformación del empleado:")
    empleado.mostrar_informacion()

if __name__ == "__main__":
    main()
