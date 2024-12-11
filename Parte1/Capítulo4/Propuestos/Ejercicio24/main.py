from esfera import Esfera
from utilidades import determinar_mayor

def main():
    # Crear las esferas con diferentes pesos
    esfera_a = Esfera("A", float(input("Ingrese el peso de la esfera A: ")))
    esfera_b = Esfera("B", float(input("Ingrese el peso de la esfera B: ")))
    esfera_c = Esfera("C", float(input("Ingrese el peso de la esfera C: ")))

    # Determinar la esfera de mayor peso
    esferas = [esfera_a, esfera_b, esfera_c]
    esfera_mayor = determinar_mayor(esferas)

    print(f"La esfera de mayor peso es la {esfera_mayor.nombre} con un peso de {esfera_mayor.peso}.")

if __name__ == "__main__":
    main()

