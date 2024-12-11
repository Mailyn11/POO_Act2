from Triangle import Triangle

# Solicitar datos por teclado
def main():
    try:
        a = float(input("Ingrese un lado a del triángulo: "))
        b = float(input("Ingrese un lado b del triángulo: "))
        c = float(input("Ingrese un lado c del triángulo: "))

        triangle = Triangle(a, b, c)
        triangle.display_properties()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
