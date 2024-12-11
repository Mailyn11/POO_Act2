from SalarioVD1 import SalarioVD1
from SalarioVD2 import SalarioVD2
from SalarioVD3 import SalarioVD3

class Salario:
    @staticmethod
    def calcular_salarios(ventas_vd1, ventas_vd2, ventas_vd3, salario_vd1, salario_vd2, salario_vd3):
        # Crear instancias de los vendedores con sus ventas y salarios
        vendedor1 = SalarioVD1(ventas_vd1, salario_vd1)
        vendedor2 = SalarioVD2(ventas_vd2, salario_vd2)
        vendedor3 = SalarioVD3(ventas_vd3, salario_vd3)
        
        # Calcular el total de ventas
        totven = ventas_vd1 + ventas_vd2 + ventas_vd3
        
        # Calcular el 33% del total de ventas
        porven = 0.33 * totven
        
        # Calcular los salarios con las condiciones de cada vendedor
        salario_final_vendedor1 = vendedor1.calcular_salario(porven)
        salario_final_vendedor2 = vendedor2.calcular_salario(porven)
        salario_final_vendedor3 = vendedor3.calcular_salario(porven)

        # Devolver los salarios ajustados y los cálculos
        return salario_final_vendedor1, salario_final_vendedor2, salario_final_vendedor3, totven, porven