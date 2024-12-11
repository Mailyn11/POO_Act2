from NumberComparator import NumberComparator

# Solicitar datos por teclado
def main():
        a = int(input("Ingresa el valor de a: "))
        b = int(input("Ingresa el valor de b: "))
        c = int(input("Ingresa el valor de c: "))

        comparator = NumberComparator(a, b, c)
        comparator.display_largest_number()

if __name__ == "__main__":
    main()