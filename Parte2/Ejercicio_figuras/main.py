from Circulo import Circulo
from Rectángulo import Rectangulo
from Cuadrado import Cuadrado
from Triangulo_rectangulo import TrianguloRectangulo
from Rombo import Rombo
from Trapecio import Trapecio

# Bloque principal
def main():
    figura1 = Circulo(2)
    figura2 = Rectangulo(1, 2)
    figura3 = Cuadrado(3)
    figura4 = TrianguloRectangulo(3, 5)
    figura5 = Rombo(2, 3, 5)
    figura6 = Trapecio(4, 2, 5, 6)

    # Círculo
    print(f"El área del círculo es: {figura1.calcular_area():.2f}")
    print(f"El perímetro del círculo es: {figura1.calcular_perimetro():.2f}\n")

    # Rectángulo
    print(f"El área del rectángulo es: {figura2.calcular_area()}")
    print(f"El perímetro del rectángulo es: {figura2.calcular_perimetro()}\n")

    # Cuadrado
    print(f"El área del cuadrado es: {figura3.calcular_area()}")
    print(f"El perímetro del cuadrado es: {figura3.calcular_perimetro()}\n")

    # Triángulo Rectángulo
    print(f"El área del triángulo es: {figura4.calcular_area()}")
    print(f"El perímetro del triángulo es: {figura4.calcular_perimetro():.2f}")
    print(figura4.determinar_tipo_triangulo(), "\n")

    # Rombo
    print(f"El área del rombo es: {figura5.calcular_area():.2f}")
    print(f"El perímetro del rombo es: {figura5.calcular_perimetro():.2f}\n")

    # Trapecio
    print(f"El área del trapecio es: {figura6.calcular_area():.2f}")
    print(f"El perímetro del trapecio es: {figura6.calcular_perimetro():.2f}\n")

if __name__ == "__main__":
    main()
