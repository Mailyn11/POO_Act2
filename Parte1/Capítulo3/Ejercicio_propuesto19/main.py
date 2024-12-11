from Triángulo_equilátero import Trianguloequilatero

def main():
    # Solicitar valor del lado por teclado
    lado = float(input("Ingrese el valor del lado del triángulo equilátero: "))

    # Crear una instancia de TrianguloEquilatero
    triangulo = Trianguloequilatero(lado)

    # Llamar a las funciones o métodos para calcular los valores
    perimetro = triangulo.obtener_perimetro()
    altura = triangulo.obtener_altura()
    area = triangulo.obtener_area()

    # Imprimir resultados
    print(f"Perímetro: {perimetro}")
    print(f"Altura: {altura}")
    print(f"Área: {area}")

if __name__ == "__main__":
    main()