from Ejercicio7 import NumberComparator

# Pedir los valores por teclado
def main():
        a = float(input("Ingrese el valor de A: "))
        b = float(input("Ingrese el valor de B: "))

        comparator = NumberComparator(a, b)
        resultado = comparator.compare()

        print(resultado)

if __name__ == "__main__":
    main()
