from Salario import Salario

def main():
    # Ingresar datos por teclado
    print("Ingrese el salario para el departamento 1: ")
    salario_depto1 = float(input())

    print("Ingrese las ventas para el departamento 1 (VD1): ")
    ventas_vd1 = float(input())

    print("Ingrese el salario para el departamento 2: ")
    salario_depto2 = float(input())

    print("Ingrese las ventas para el departamento 2 (VD2): ")
    ventas_vd2 = float(input())

    print("Ingrese el salario para el departamento 3: ")
    salario_depto3 = float(input())

    print("Ingrese las ventas para el departamento 3 (VD3): ")
    ventas_vd3 = float(input())

    # Calcular salarios usando el método estático de la clase Salario
    salario_final_vendedor1, salario_final_vendedor2, salario_final_vendedor3, total_ventas, porcentaje_ventas = Salario.calcular_salarios(ventas_vd1, ventas_vd2, ventas_vd3, salario_depto1, salario_depto2, salario_depto3)

    # Imprimir resultados
    print(f"VENTAS TOTALES (TOTVEN): {total_ventas}")
    print(f"PORCENTAJE DE VENTAS (PORVEN): {porcentaje_ventas}")
    print(f"SALARIO VENDEDOR DEPTO. 1: {salario_final_vendedor1}")
    print(f"SALARIO VENDEDOR DEPTO. 2: {salario_final_vendedor2}")
    print(f"SALARIO VENDEDOR DEPTO. 3: {salario_final_vendedor3}")

if __name__ == "__main__":
    main()